package com.jarvis.core

import android.app.Activity
import android.os.Bundle
import android.graphics.Color
import android.view.Gravity
import android.widget.LinearLayout
import android.widget.TextView

class MainActivity : Activity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        val root = LinearLayout(this)
        root.orientation = LinearLayout.VERTICAL
        root.gravity = Gravity.CENTER
        root.setPadding(40, 40, 40, 40)

        val title = TextView(this)
        title.text = "JARVIS"
        title.textSize = 42f
        title.setTextColor(Color.WHITE)
        title.gravity = Gravity.CENTER

        val status = TextView(this)
        status.text = "\n● CORE ONLINE\n\nAwaiting command..."
        status.textSize = 20f
        status.setTextColor(Color.WHITE)
        status.gravity = Gravity.CENTER

        root.setBackgroundColor(Color.BLACK)

        root.addView(title)
        root.addView(status)

        setContentView(root)
    }
}
