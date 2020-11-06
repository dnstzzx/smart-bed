package com.dnstzzx.babynotifier

import android.app.Service
import android.content.Intent
import android.os.Bundle
import android.os.Vibrator
import androidx.appcompat.app.AppCompatActivity;
import com.google.gson.Gson

import kotlinx.coroutines.*
import android.media.MediaPlayer
import kotlinx.android.synthetic.main.activity_main.*


class MainActivity : AppCompatActivity() {
    lateinit var info: BabyInfo
    var success = false
    var isVirating = false
    var isPlayingMusic = false
    var state:String = ""
    lateinit var vib:Vibrator
    lateinit var mediaPlayer: MediaPlayer

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        setSupportActionBar(toolbar)

        supportActionBar?.title = Variables.PRODUCT_NAME

        vib = this@MainActivity.getSystemService(Service.VIBRATOR_SERVICE) as Vibrator
        mediaPlayer = MediaPlayer.create(this, R.raw.beep)
        //mediaPlayer.prepare()

        mediaPlayer.setOnCompletionListener { mediaPlayer ->
            if(isPlayingMusic){

                //mediaPlayer.seekTo(0)
                mediaPlayer.start()
            }
        }

        button_openVideo.setOnClickListener {
            setPlayAudio(false)
            setVibrate(false)
            val intent = Intent(this@MainActivity, VideoActivity::class.java)
            startActivity(intent)
        }


        GlobalScope.launch {
            while(!this@MainActivity.isDestroyed){
                loop()
                delay(100)
            }
        }
    }

    suspend fun reflesh(){
        success =true
        try {
            val json = NetUtils.get(Variables.SERVER + "/state")
            val gson = Gson()
            info = gson.fromJson(json, BabyInfo::class.java)
            if (info.bed_wet){
                state = "宝宝尿床"
            }
            state = when(info.deep_state){
                0 -> "一切安好"
                1 -> "头被盖住"
                2 -> "头枕分离"
                3 ->  if (switch_detect_quilt_out.isChecked) "宝宝踢被" else "一切安好"
                else -> "一切安好"
            }
            if(info.baby_outbed){
                state = "宝宝坐起"
            }

        }catch(ex:Exception){
            success = false
            return
        }
    }

    suspend fun loop(){
        reflesh()
        if(!success) return
        updateToUI()
        checkAlarming()

    }

    fun updateToUI(){
        runOnUiThread( Runnable {
            if(success){
                label_temperature.text = info.temperature.toString() + " ℃"
                label_humidity.text = info.humidity.toString() + " %"
                label_state.text = state
                img_state.setImageResource(if (state == "一切安好") R.drawable.yes else R.drawable.att)
            }
        })

    }

    fun checkAlarming(){

        if (!switch_Alarm.isChecked){
            isPlayingMusic = false
            setVibrate(false)
            return
        }
        val alarm = (state != "一切安好")
        setPlayAudio(alarm)
        setVibrate(alarm)

    }

    fun setPlayAudio(playing: Boolean){
        if(isPlayingMusic != playing){
            isPlayingMusic = playing
            when(playing){
                true ->  mediaPlayer.start()
                false -> mediaPlayer.stop()
            }
        }
    }



    fun setVibrate(virating:Boolean){
        if(isVirating != virating){
            isVirating = virating
            when(virating){
                true -> vib.vibrate(longArrayOf(1000,1000), 0)
                false -> vib.cancel()
            }
        }
    }




}
