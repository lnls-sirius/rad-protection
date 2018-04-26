<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<databrowser>
    <title></title>
    <save_changes>true</save_changes>
    <show_legend>false</show_legend>
    <show_toolbar>true</show_toolbar>
    <grid>false</grid>
    <scroll>true</scroll>
    <update_period>3.0</update_period>
    <scroll_step>5</scroll_step>
    <start>-30 min</start>
    <end>now</end>
    <archive_rescale>NONE</archive_rescale>
    <background>
        <red>255</red>
        <green>255</green>
        <blue>255</blue>
    </background>
    <title_font>Ubuntu|16|1</title_font>
    <label_font>Ubuntu|11|1</label_font>
    <scale_font>Ubuntu|10|0</scale_font>
    <legend_font>Ubuntu|10|0</legend_font>
    <axes>
        <axis>
            <visible>true</visible>
            <name>uSv/h</name>
            <use_axis_name>true</use_axis_name>
            <use_trace_names>false</use_trace_names>
            <right>false</right>
            <color>
                <red>0</red>
                <green>0</green>
                <blue>0</blue>
            </color>
            <label_font>|10|0</label_font>
            <scale_font>|10|0</scale_font>
            <min>0.0017598058252427662</min>
            <max>0.3515598058252427</max>
            <grid>false</grid>
            <autoscale>false</autoscale>
            <log_scale>false</log_scale>
        </axis>
    </axes>
    <annotations>
    </annotations>
    <pvlist>
        <pv>
            <display_name>RAD:Berthold:Gamma</display_name>
            <visible>true</visible>
            <name>RAD:Berthold:Gamma</name>
            <axis>0</axis>
            <color>
                <red>0</red>
                <green>255</green>
                <blue>255</blue>
            </color>
            <trace_type>SINGLE_LINE</trace_type>
            <linewidth>2</linewidth>
            <point_type>NONE</point_type>
            <point_size>2</point_size>
            <waveform_index>0</waveform_index>
            <period>0.0</period>
            <ring_size>5000</ring_size>
            <request>RAW</request>
            <archive>
                <name>All</name>
                <url>pbraw://10.0.4.57:11998/retrieval</url>
                <key>1</key>
            </archive>
        </pv>
        <pv>
            <display_name>RAD:Berthold:TotalDoseRate</display_name>
            <visible>true</visible>
            <name>RAD:Berthold:TotalDoseRate</name>
            <axis>0</axis>
            <color>
                <red>255</red>
                <green>0</green>
                <blue>255</blue>
            </color>
            <trace_type>SINGLE_LINE</trace_type>
            <linewidth>2</linewidth>
            <point_type>NONE</point_type>
            <point_size>2</point_size>
            <waveform_index>0</waveform_index>
            <period>0.0</period>
            <ring_size>5000</ring_size>
            <request>RAW</request>
            <archive>
                <name>All</name>
                <url>pbraw://10.0.4.57:11998/retrieval</url>
                <key>1</key>
            </archive>
        </pv>
        <pv>
            <display_name>RAD:Berthold:TotalNeutronRate</display_name>
            <visible>true</visible>
            <name>RAD:Berthold:TotalNeutronRate</name>
            <axis>0</axis>
            <color>
                <red>255</red>
                <green>255</green>
                <blue>0</blue>
            </color>
            <trace_type>SINGLE_LINE</trace_type>
            <linewidth>2</linewidth>
            <point_type>NONE</point_type>
            <point_size>2</point_size>
            <waveform_index>0</waveform_index>
            <period>0.0</period>
            <ring_size>5000</ring_size>
            <request>RAW</request>
            <archive>
                <name>All</name>
                <url>pbraw://10.0.4.57:11998/retrieval</url>
                <key>1</key>
            </archive>
        </pv>
        <pv>
            <display_name>RAD:ELSE:TotalDoseRate</display_name>
            <visible>true</visible>
            <name>RAD:ELSE:TotalDoseRate</name>
            <axis>0</axis>
            <color>
                <red>0</red>
                <green>255</green>
                <blue>0</blue>
            </color>
            <trace_type>SINGLE_LINE</trace_type>
            <linewidth>2</linewidth>
            <point_type>NONE</point_type>
            <point_size>2</point_size>
            <waveform_index>0</waveform_index>
            <period>0.0</period>
            <ring_size>5000</ring_size>
            <request>RAW</request>
            <archive>
                <name>All</name>
                <url>pbraw://10.0.4.57:11998/retrieval</url>
                <key>1</key>
            </archive>
        </pv>
        <pv>
            <display_name>RAD:THERMO:TotalDoseRate</display_name>
            <visible>true</visible>
            <name>RAD:THERMO:TotalDoseRate</name>
            <axis>0</axis>
            <color>
                <red>0</red>
                <green>0</green>
                <blue>255</blue>
            </color>
            <trace_type>SINGLE_LINE</trace_type>
            <linewidth>2</linewidth>
            <point_type>NONE</point_type>
            <point_size>2</point_size>
            <waveform_index>0</waveform_index>
            <period>0.0</period>
            <ring_size>5000</ring_size>
            <request>RAW</request>
            <archive>
                <name>All</name>
                <url>pbraw://10.0.4.57:11998/retrieval</url>
                <key>1</key>
            </archive>
        </pv>
        <pv>
            <display_name>RAD:ELSE:Gamma</display_name>
            <visible>true</visible>
            <name>RAD:ELSE:Gamma</name>
            <axis>0</axis>
            <color>
                <red>255</red>
                <green>128</green>
                <blue>0</blue>
            </color>
            <trace_type>SINGLE_LINE</trace_type>
            <linewidth>2</linewidth>
            <point_type>NONE</point_type>
            <point_size>2</point_size>
            <waveform_index>0</waveform_index>
            <period>0.0</period>
            <ring_size>5000</ring_size>
            <request>RAW</request>
            <archive>
                <name>All</name>
                <url>pbraw://10.0.4.57:11998/retrieval</url>
                <key>1</key>
            </archive>
        </pv>
        <pv>
            <display_name>RAD:ELSE:Neutron</display_name>
            <visible>true</visible>
            <name>RAD:ELSE:Neutron</name>
            <axis>0</axis>
            <color>
                <red>150</red>
                <green>0</green>
                <blue>0</blue>
            </color>
            <trace_type>SINGLE_LINE</trace_type>
            <linewidth>2</linewidth>
            <point_type>NONE</point_type>
            <point_size>2</point_size>
            <waveform_index>0</waveform_index>
            <period>0.0</period>
            <ring_size>5000</ring_size>
            <request>RAW</request>
            <archive>
                <name>All</name>
                <url>pbraw://10.0.4.57:11998/retrieval</url>
                <key>1</key>
            </archive>
        </pv>
        <pv>
            <display_name>RAD:THERMO:Neutron</display_name>
            <visible>true</visible>
            <name>RAD:THERMO:Neutron</name>
            <axis>0</axis>
            <color>
                <red>159</red>
                <green>150</green>
                <blue>150</blue>
            </color>
            <trace_type>SINGLE_LINE</trace_type>
            <linewidth>2</linewidth>
            <point_type>NONE</point_type>
            <point_size>2</point_size>
            <waveform_index>0</waveform_index>
            <period>0.0</period>
            <ring_size>5000</ring_size>
            <request>RAW</request>
            <archive>
                <name>All</name>
                <url>pbraw://10.0.4.57:11998/retrieval</url>
                <key>1</key>
            </archive>
        </pv>
        <pv>
            <display_name>RAD:THERMO:Gamma</display_name>
            <visible>true</visible>
            <name>RAD:THERMO:Gamma</name>
            <axis>0</axis>
            <color>
                <red>0</red>
                <green>0</green>
                <blue>0</blue>
            </color>
            <trace_type>SINGLE_LINE</trace_type>
            <linewidth>2</linewidth>
            <point_type>NONE</point_type>
            <point_size>2</point_size>
            <waveform_index>0</waveform_index>
            <period>0.0</period>
            <ring_size>5000</ring_size>
            <request>RAW</request>
            <archive>
                <name>All</name>
                <url>pbraw://10.0.4.57:11998/retrieval</url>
                <key>1</key>
            </archive>
        </pv>
        <pv>
            <display_name>RAD:Berthold:HighEnergyNeutrons</display_name>
            <visible>true</visible>
            <name>RAD:Berthold:HighEnergyNeutrons</name>
            <axis>0</axis>
            <color>
                <red>0</red>
                <green>128</green>
                <blue>0</blue>
            </color>
            <trace_type>SINGLE_LINE</trace_type>
            <linewidth>2</linewidth>
            <point_type>NONE</point_type>
            <point_size>2</point_size>
            <waveform_index>0</waveform_index>
            <period>0.0</period>
            <ring_size>5000</ring_size>
            <request>RAW</request>
            <archive>
                <name>All</name>
                <url>pbraw://10.0.4.57:11998/retrieval</url>
                <key>1</key>
            </archive>
        </pv>
        <formula>
            <display_name>Bg Berthold</display_name>
            <visible>true</visible>
            <name>RAD:Berthold:BG</name>
            <axis>0</axis>
            <color>
                <red>255</red>
                <green>0</green>
                <blue>0</blue>
            </color>
            <trace_type>AREA</trace_type>
            <linewidth>2</linewidth>
            <point_type>NONE</point_type>
            <point_size>2</point_size>
            <waveform_index>0</waveform_index>
            <formula>x1 - x1+0.113</formula>
            <input>
                <pv>RAD:Berthold:Gamma</pv>
                <name>x1</name>
            </input>
        </formula>
        <formula>
            <display_name>RAD:THERMO:BG</display_name>
            <visible>true</visible>
            <name>RAD:THERMO:BG</name>
            <axis>0</axis>
            <color>
                <red>255</red>
                <green>232</green>
                <blue>173</blue>
            </color>
            <trace_type>AREA</trace_type>
            <linewidth>2</linewidth>
            <point_type>NONE</point_type>
            <point_size>2</point_size>
            <waveform_index>0</waveform_index>
            <formula>x5-x5</formula>
            <input>
                <pv>RAD:THERMO:TotalDoseRate</pv>
                <name>x5</name>
            </input>
        </formula>
        <formula>
            <display_name>RAD:ELSE:BG</display_name>
            <visible>true</visible>
            <name>RAD:ELSE:BG</name>
            <axis>0</axis>
            <color>
                <red>173</red>
                <green>216</green>
                <blue>230</blue>
            </color>
            <trace_type>AREA</trace_type>
            <linewidth>2</linewidth>
            <point_type>NONE</point_type>
            <point_size>2</point_size>
            <waveform_index>0</waveform_index>
            <formula>x4-x4</formula>
            <input>
                <pv>RAD:ELSE:TotalDoseRate</pv>
                <name>x4</name>
            </input>
        </formula>
    </pvlist>
</databrowser>