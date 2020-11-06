package com.dnstzzx.babynotifier

data class BabyInfo (val temperature: Int,
                     val humidity: Int,
                     val bed_wet: Boolean,
                     val baby_outbed: Boolean,

                     val deep_state: Int)