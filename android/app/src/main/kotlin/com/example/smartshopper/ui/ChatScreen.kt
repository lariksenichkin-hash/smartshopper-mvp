package com.example.smartshopper.ui

import androidx.compose.foundation.layout.*
import androidx.compose.material.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import com.example.smartshopper.network.ApiService
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch

@Composable
fun ChatScreen() {
    var query by remember { mutableStateOf("") }
    var messages by remember { mutableStateOf(listOf<String>()) }

    Column(modifier = Modifier.fillMaxSize().padding(16.dp)) {
        Column(modifier = Modifier.weight(1f)) {
            for (m in messages) {
                Text(text = m)
                Spacer(modifier = Modifier.height(8.dp))
            }
        }

        Row(modifier = Modifier.fillMaxWidth()) {
            TextField(value = query, onValueChange = { query = it }, modifier = Modifier.weight(1f))
            Spacer(modifier = Modifier.width(8.dp))
            Button(onClick = {
                messages = messages + "You: $query"
                CoroutineScope(Dispatchers.IO).launch {
                    val resp = ApiService.search(query)
                    // update messages on main thread
                    kotlinx.coroutines.CoroutineScope(Dispatchers.Main).launch {
                        messages = messages + "AI: $resp"
                    }
                }
            }) {
                Text("Send")
            }
        }
    }
}
