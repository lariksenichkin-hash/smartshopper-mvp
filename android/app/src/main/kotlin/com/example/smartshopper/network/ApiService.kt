package com.example.smartshopper.network

import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import okhttp3.MediaType.Companion.toMediaTypeOrNull
import okhttp3.OkHttpClient
import okhttp3.Request
import okhttp3.RequestBody.Companion.toRequestBody

object ApiService {
    private val client = OkHttpClient()
    private const val BASE_URL = "http://10.0.2.2:8000/api"

    suspend fun search(query: String): String = withContext(Dispatchers.IO) {
        val json = "{\"query\": \"$query\"}"
        val reqBody = json.toRequestBody("application/json".toMediaTypeOrNull())
        val request = Request.Builder().url("$BASE_URL/search").post(reqBody).build()
        val resp = client.newCall(request).execute()
        return@withContext resp.body?.string() ?: "{}"
    }
}
