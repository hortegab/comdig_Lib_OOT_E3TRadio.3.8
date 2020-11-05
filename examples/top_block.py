#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Top Block
# GNU Radio version: 3.8.1.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
import numpy
from gnuradio import filter
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import E3TRadio
import wform  # embedded python module
from gnuradio import qtgui

class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.Sps = Sps = 8
        self.Rb = Rb = 32000
        self.samp_rate = samp_rate = Rb*Sps
        self.rolloff4 = rolloff4 = 0.
        self.rolloff3 = rolloff3 = 0.35
        self.rolloff2 = rolloff2 = 0.5
        self.rolloff1 = rolloff1 = 1.0
        self.ntaps = ntaps = 128

        ##################################################
        # Blocks
        ##################################################
        self.pestana = Qt.QTabWidget()
        self.pestana_widget_0 = Qt.QWidget()
        self.pestana_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.pestana_widget_0)
        self.pestana_grid_layout_0 = Qt.QGridLayout()
        self.pestana_layout_0.addLayout(self.pestana_grid_layout_0)
        self.pestana.addTab(self.pestana_widget_0, 'Datos')
        self.pestana_widget_1 = Qt.QWidget()
        self.pestana_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.pestana_widget_1)
        self.pestana_grid_layout_1 = Qt.QGridLayout()
        self.pestana_layout_1.addLayout(self.pestana_grid_layout_1)
        self.pestana.addTab(self.pestana_widget_1, 'Espectro')
        self.pestana_widget_2 = Qt.QWidget()
        self.pestana_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.pestana_widget_2)
        self.pestana_grid_layout_2 = Qt.QGridLayout()
        self.pestana_layout_2.addLayout(self.pestana_grid_layout_2)
        self.pestana.addTab(self.pestana_widget_2, 'Diagrama de Ojo')
        self.top_grid_layout.addWidget(self.pestana)
        self.qtgui_time_sink_x_0_0_0_0_0 = qtgui.time_sink_f(
            ntaps, #size
            samp_rate, #samp_rate
            "Wave Forming", #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0_0_0.set_y_axis(-3, 3)

        self.qtgui_time_sink_x_0_0_0_0_0.set_y_label('RC Filter', "")

        self.qtgui_time_sink_x_0_0_0_0_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_AUTO, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0_0_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0_0_0_0_0.enable_stem_plot(False)


        labels = ['Senal0', 'Senal1', 'RC, rollof=0.5', 'RC, rollof=0.35', 'RRC, rollof=0',
            '', '', '', '', '']
        widths = [3, 3, 3, 3, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.pestana_layout_0.addWidget(self._qtgui_time_sink_x_0_0_0_0_0_win)
        self.low_pass_filter_0_0 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                (Rb/2)*(1+rolloff2),
                (Rb/2)*(1+rolloff2)/8,
                firdes.WIN_HAMMING,
                6.76))
        self.interp_fir_filter_xxx_0_0_0_0_0_0 = filter.interp_fir_filter_fff(Sps, wform.rcos(Sps,ntaps,rolloff1))
        self.interp_fir_filter_xxx_0_0_0_0_0_0.declare_sample_delay(0)
        self.blocks_stream_to_vector_0_0 = blocks.stream_to_vector(gr.sizeof_float*1, Sps*256)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_ff(1/1.5)
        self.blocks_int_to_float_0 = blocks.int_to_float(1, 1)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, int(Sps/2))
        self.blocks_add_xx_0_0 = blocks.add_vff(1)
        self.analog_random_source_x_0 = blocks.vector_source_i(list(map(int, numpy.random.randint(0, 2, 1000000))), True)
        self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_GAUSSIAN, 0.15, 0)
        self.E3TRadio_vec_diagrama_ojo_f_0 = E3TRadio.vec_diagrama_ojo_f(Sps, samp_rate, Sps*256)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_int_to_float_0, 0))
        self.connect((self.blocks_add_xx_0_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_stream_to_vector_0_0, 0))
        self.connect((self.blocks_int_to_float_0, 0), (self.interp_fir_filter_xxx_0_0_0_0_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.qtgui_time_sink_x_0_0_0_0_0, 0))
        self.connect((self.blocks_stream_to_vector_0_0, 0), (self.E3TRadio_vec_diagrama_ojo_f_0, 0))
        self.connect((self.interp_fir_filter_xxx_0_0_0_0_0_0, 0), (self.blocks_add_xx_0_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.blocks_add_xx_0_0, 1))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps
        self.set_samp_rate(self.Rb*self.Sps)
        self.blocks_delay_0.set_dly(int(self.Sps/2))
        self.interp_fir_filter_xxx_0_0_0_0_0_0.set_taps(wform.rcos(self.Sps,self.ntaps,self.rolloff1))

    def get_Rb(self):
        return self.Rb

    def set_Rb(self, Rb):
        self.Rb = Rb
        self.set_samp_rate(self.Rb*self.Sps)
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, (self.Rb/2)*(1+self.rolloff2), (self.Rb/2)*(1+self.rolloff2)/8, firdes.WIN_HAMMING, 6.76))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, (self.Rb/2)*(1+self.rolloff2), (self.Rb/2)*(1+self.rolloff2)/8, firdes.WIN_HAMMING, 6.76))
        self.qtgui_time_sink_x_0_0_0_0_0.set_samp_rate(self.samp_rate)

    def get_rolloff4(self):
        return self.rolloff4

    def set_rolloff4(self, rolloff4):
        self.rolloff4 = rolloff4

    def get_rolloff3(self):
        return self.rolloff3

    def set_rolloff3(self, rolloff3):
        self.rolloff3 = rolloff3

    def get_rolloff2(self):
        return self.rolloff2

    def set_rolloff2(self, rolloff2):
        self.rolloff2 = rolloff2
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, (self.Rb/2)*(1+self.rolloff2), (self.Rb/2)*(1+self.rolloff2)/8, firdes.WIN_HAMMING, 6.76))

    def get_rolloff1(self):
        return self.rolloff1

    def set_rolloff1(self, rolloff1):
        self.rolloff1 = rolloff1
        self.interp_fir_filter_xxx_0_0_0_0_0_0.set_taps(wform.rcos(self.Sps,self.ntaps,self.rolloff1))

    def get_ntaps(self):
        return self.ntaps

    def set_ntaps(self, ntaps):
        self.ntaps = ntaps
        self.interp_fir_filter_xxx_0_0_0_0_0_0.set_taps(wform.rcos(self.Sps,self.ntaps,self.rolloff1))



def main(top_block_cls=top_block, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
