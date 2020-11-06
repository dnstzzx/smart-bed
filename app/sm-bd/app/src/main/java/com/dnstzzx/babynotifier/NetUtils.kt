package com.dnstzzx.babynotifier

import android.accounts.NetworkErrorException
import com.dnstzzx.babynotifier.NetUtils.getStringFromInputStream

import java.io.ByteArrayOutputStream
import java.io.IOException
import java.io.InputStream
import java.io.OutputStream
import java.net.HttpURLConnection
import java.net.URL

object NetUtils {
    @Throws(IOException::class, NetworkErrorException::class)
    fun post(url: String, content: String): String {
        var conn: HttpURLConnection? = null
        try {
            // 创建一个URL对象
            val mURL = URL(url)
            // 调用URL的openConnection()方法,获取HttpURLConnection对象
            conn = mURL.openConnection() as HttpURLConnection

            conn.requestMethod = "POST"// 设置请求方法为post
            conn.readTimeout = 5000// 设置读取超时为5秒
            conn.connectTimeout = 10000// 设置连接网络超时为10秒
            conn.doOutput = true// 设置此方法,允许向服务器输出内容

            // post请求的参数
            // 获得一个输出流,向服务器写数据,默认情况下,系统不允许向服务器输出内容
            val out = conn.outputStream// 获得一个输出流,向服务器写数据
            out.write(content.toByteArray())
            out.flush()
            out.close()

            val responseCode = conn.responseCode// 调用此方法就不必再使用conn.connect()方法
            if (responseCode == 200) {

                val `is` = conn.inputStream
                return getStringFromInputStream(`is`)
            } else {
                throw NetworkErrorException("response status is $responseCode")
            }

        } finally {
            conn?.disconnect()
        }
    }

    suspend fun get(url: String): String? {
        var conn: HttpURLConnection? = null
        try {
            // 利用string url构建URL对象
            val mURL = URL(url)
            conn = mURL.openConnection() as HttpURLConnection

            conn.requestMethod = "GET"
            conn.readTimeout = 5000
            conn.connectTimeout = 10000

            val responseCode = conn.responseCode
            if (responseCode == 200) {

                val `is` = conn.inputStream
                return getStringFromInputStream(`is`)
            } else {
                throw NetworkErrorException("response status is $responseCode")
            }

        } catch (e: Exception) {
            e.printStackTrace()
            return null
        } finally {
            conn?.disconnect()
        }

        return null
    }

    @Throws(IOException::class)
    private fun getStringFromInputStream(`is`: InputStream): String {
        val os = ByteArrayOutputStream()
        // 模板代码 必须熟练
        val buffer = ByteArray(1024)
        var len = -1

        len = `is`.read(buffer)
        while (len != -1) {
            os.write(buffer, 0, len)
            len = `is`.read(buffer)
        }
        `is`.close()
        val state = os.toString()// 把流中的数据转换成字符串,采用的编码是utf-8(模拟器默认编码)
        os.close()
        return state
    }

    @Throws(IOException::class)
    fun getImageViewInputStream(path:String): InputStream? {
        var inputStream: InputStream? = null
        val url = URL(path)                    //服务器地址
        if (url != null) {
            //打开连接
            val httpURLConnection = url.openConnection() as HttpURLConnection
            httpURLConnection.setConnectTimeout(3000)//设置网络连接超时的时间为3秒
            httpURLConnection.setRequestMethod("GET")        //设置请求方法为GET
            httpURLConnection.setDoInput(true)                //打开输入流
            val responseCode = httpURLConnection.getResponseCode()    // 获取服务器响应值
            if (responseCode == HttpURLConnection.HTTP_OK) {        //正常连接
                inputStream = httpURLConnection.getInputStream()        //获取输入流
            }
        }
        return inputStream
    }
}