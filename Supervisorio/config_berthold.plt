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
    <start>-2 minutes 0.0 seconds</start>
    <end>now</end>
    <archive_rescale>NONE</archive_rescale>
    <foreground>
        <red>0</red>
        <green>0</green>
        <blue>0</blue>
    </foreground>
    <background>
        <red>255</red>
        <green>255</green>
        <blue>255</blue>
    </background>
    <title_font>Liberation Sans|20|1</title_font>
    <label_font>Liberation Sans|14|1</label_font>
    <scale_font>Liberation Sans|12|0</scale_font>
    <legend_font>Liberation Sans|14|0</legend_font>
    <axes>
        <axis>
            <visible>true</visible>
            <name>Value 1</name>
            <use_axis_name>false</use_axis_name>
            <use_trace_names>true</use_trace_names>
            <right>false</right>
            <color>
                <red>0</red>
                <green>0</green>
                <blue>0</blue>
            </color>
            <min>-0.004745</min>
            <max>0.099645</max>
            <grid>false</grid>
            <autoscale>true</autoscale>
            <log_scale>false</log_scale>
        </axis>
    </axes>
    <annotations>
    </annotations>
    <pvlist>
        <pv>
            <display_name>RAD:Berthold:Gamma-T</display_name>
            <visible>true</visible>
            <name>RAD:Berthold:Gamma-T</name>
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
            <period>1.0</period>
            <ring_size>5000</ring_size>
            <request>RAW</request>
            <archive>
                <name>All</name>
                <url>pbraw://10.0.6.57:11998/retrieval</url>
                <key>1</key>
            </archive>
        </pv>
    </pvlist>
</databrowser>