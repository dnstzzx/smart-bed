import torch
from torch.nn import functional as F
from tqdm import tqdm

import model
from data import MyDataSet
from model import device

batch_size = 64
epoch_a = 20
learning_rate =0.001

dataset_train = MyDataSet( split='train')
dataset_test = MyDataSet( split='test')
net = model.MyNet().to(device)

def one_hot_to_label(one_hot):
    return torch.argmax(one_hot, dim= -1).cpu().item()

def validate(net, data_loader):
    with torch.no_grad():
        net.eval()
        corrs = 0
        for rgb, label in data_loader:
            y = net(rgb)
            for sample_id in range(label.shape[0]):
                if label[sample_id].item() == one_hot_to_label(y[sample_id]):
                    corrs += 1
        net.train()
        return [corrs / len(data_loader.dataset) ]

def train(net, dataset_train, dataset_test):
    dataloader_train = torch.utils.data.DataLoader(dataset_train, batch_size=batch_size, shuffle=True, num_workers=0)
    dataloader_test = torch.utils.data.DataLoader(dataset_test, batch_size=batch_size, shuffle=True, num_workers=0)

    optimizer_finetune = torch.optim.SGD(net.fc.parameters(), learning_rate)
    optimizer = torch.optim.Adam(
        net.parameters(),
        lr=learning_rate,
        betas=(0.9, 0.999),
        eps=1e-08
    )

    scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=20, gamma=0.7)

    ''' fine tune '''
    for epoch in range(epoch_a):
        for batch_id, data in tqdm(enumerate(dataloader_train, 0), total=len(dataloader_train), smoothing=0.9):
            rgb, label = data
            optimizer_finetune.zero_grad()
            net = net.train()
            y = net(rgb)

            pred = F.log_softmax(y, -1)
            loss = F.nll_loss(pred, label.to(device))
            loss.backward()
            optimizer_finetune.step()
        training_accs = validate(net, dataloader_train)
        testing_accs = validate(net, dataloader_test)

        tqdm.write(f'{training_accs=}  loss = {loss.item()}')
        tqdm.write(f'{testing_accs=}')

    for epoch in range(epoch_a):
        scheduler.step()
        
        for batch_id, data in tqdm(enumerate(dataloader_train, 0), total=len(dataloader_train), smoothing=0.9):
            rgb, label = data
            optimizer.zero_grad()
            net = net.train()
            y = net(rgb)
            pred = F.log_softmax(y, -1)
            loss = F.nll_loss(pred, label.to(device))
            loss.backward()
            optimizer.step()

        training_accs = validate(net, dataloader_train)
        testing_accs = validate(net, dataloader_test)

        tqdm.write(f'{training_accs=}  {testing_accs=} loss = {loss.item()}')
        torch.save(net, 'model.pth')

if __name__ == '__main__':
    train(net, dataset_train, dataset_test)
