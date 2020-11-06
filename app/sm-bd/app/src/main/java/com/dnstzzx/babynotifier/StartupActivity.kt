package com.dnstzzx.babynotifier

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch

class StartupActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_startup)
        var actionBar=getActionBar()
        actionBar?.hide()

        GlobalScope.launch {
            testServer()
        }
    }


    suspend fun testServer(){
        var ret = NetUtils.get(Variables.SERVER+"/hello")
        if(ret == "hello"){
            delay(1000)
            val intent = Intent(this@StartupActivity, MainActivity::class.java)
            startActivity(intent)
            finish()
        }
    }
}
