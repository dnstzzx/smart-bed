package com.dnstzzx.babynotifier

import android.graphics.Bitmap
import android.graphics.BitmapFactory
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.graphics.drawable.Drawable
import kotlinx.android.synthetic.main.activity_video.*
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.launch
import java.io.InputStream
import java.lang.Exception
import java.net.URL
import java.net.HttpURLConnection.HTTP_OK


class VideoActivity : AppCompatActivity() {
    val videopath = Variables.SERVER + "/video"

    var process:Boolean = true

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_video)

        GlobalScope.launch {
            while (!this@VideoActivity.isDestroyed){
                loop()
            }
        }
    }

    override fun onBackPressed() {
        process = false
        super.onBackPressed()
    }

    suspend fun loop(){
        var inputStream: InputStream? = null
        try {
            inputStream = NetUtils.getImageViewInputStream(videopath)
            val bitmap:Bitmap = BitmapFactory.decodeStream(inputStream)
            runOnUiThread { imageView.setImageBitmap(bitmap) }

        }catch (ex:Exception){
            ex.printStackTrace()
        }finally {
            inputStream?.close()
        }




    }





}
