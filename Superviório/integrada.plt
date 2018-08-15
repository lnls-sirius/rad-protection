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
    <start>-4 hours 0.0 seconds</start>
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
            <name>uSv</name>
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
            <min>-0.0217</min>
            <max>2.5</max>
            <grid>false</grid>
            <autoscale>false</autoscale>
            <log_scale>false</log_scale>
        </axis>
    </axes>
    <annotations>
    </annotations>
    <pvlist>
        <pv>
            <display_name>RAD:ELSE:TotalDoseRate:Dose-T</display_name>
            <visible>true</visible>
            <name>RAD:ELSE:TotalDoseRate:Dose-T</name>
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
                <url>pbraw://10.0.6.57:11998/retrieval</url>
                <key>1</key>
            </archive>
        </pv>
        <pv>
            <display_name>RAD:Thermo1:TotalDoseRate:Dose-T</display_name>
            <visible>true</visible>
            <name>RAD:Thermo1:TotalDoseRate:Dose-T</name>
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
        </pv>
        <pv>
            <display_name>RAD:Berthold:TotalDoseRate:Dose-T</display_name>
            <visible>true</visible>
            <name>RAD:Berthold:TotalDoseRate:Dose-T</name>
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
                <url>pbraw://10.0.6.57:11998/retrieval</url>
                <key>1</key>
            </archive>
        </pv>
        <pv>
            <display_name>RAD:Thermo1:Gamma:Dose-T</display_name>
            <visible>true</visible>
            <name>RAD:Thermo1:Gamma:Dose-T</name>
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
        </pv>
        <pv>
            <display_name>RAD:Thermo1:Neutron:Dose-T</display_name>
            <visible>true</visible>
            <name>RAD:Thermo1:Neutron:Dose-T</name>
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
        </pv>
        <pv>
            <display_name>RAD:ELSE:Gamma:Dose-T</display_name>
            <visible>true</visible>
            <name>RAD:ELSE:Gamma:Dose-T</name>
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
                <url>pbraw://10.0.6.57:11998/retrieval</url>
                <key>1</key>
            </archive>
        </pv>
        <pv>
            <display_name>RAD:ELSE:Neutron:Dose-T</display_name>
            <visible>true</visible>
            <name>RAD:ELSE:Neutron:Dose-T</name>
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
                <url>pbraw://10.0.6.57:11998/retrieval</url>
                <key>1</key>
            </archive>
        </pv>
        <pv>
            <display_name>RAD:Berthold:Gamma:Dose-T</display_name>
            <visible>true</visible>
            <name>RAD:Berthold:Gamma:Dose-T</name>
            <axis>0</axis>
            <color>
                <red>30</red>
                <green>255</green>
                <blue>253</blue>
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
                <url>pbraw://10.0.6.57:11998/retrieval</url>
                <key>1</key>
            </archive>
        </pv>
        <pv>
            <display_name>RAD:Berthold:TotalNeutronRate:Dose-T</display_name>
            <visible>true</visible>
            <name>RAD:Berthold:TotalNeutronRate:Dose-T</name>
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
                <url>pbraw://10.0.6.57:11998/retrieval</url>
                <key>1</key>
            </archive>
        </pv>
        <formula>
            <display_name>Limite</display_name>
            <visible>true</visible>
            <name>B</name>
            <axis>0</axis>
            <color>
                <red>255</red>
                <green>0</green>
                <blue>0</blue>
            </color>
            <trace_type>SINGLE_LINE</trace_type>
            <linewidth>2</linewidth>
            <point_type>NONE</point_type>
            <point_size>2</point_size>
            <waveform_index>0</waveform_index>
            <formula>x3-x3+2</formula>
            <input>
                <pv>RAD:Berthold:TotalDoseRate:Dose-T</pv>
                <name>x3</name>
            </input>
        </formula>
    </pvlist>
</databrowser>