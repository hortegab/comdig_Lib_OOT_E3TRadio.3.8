#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Top Block
# GNU Radio version: 3.9.0.0

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

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt5 import Qt
from gnuradio import qtgui
import sip
from b_binary_bipolar_source1_f import b_binary_bipolar_source1_f  # grc-generated hier_block
from gnuradio import blocks
from gnuradio import fft
from gnuradio.fft import window
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import E3TRadio
import numpy
import wform  # embedded python module



from gnuradio import qtgui

class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block", catch_exceptions=True)
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
        self.samp_rate = samp_rate = 1953125
        self.Sps = Sps = 32
        self.run_stop = run_stop = True
        self.h = h = wform.rect(Sps)
        self.Rb = Rb = samp_rate/Sps
        self.N = N = 16*Sps
        self.Mean_reset = Mean_reset = 1
        self.Ensayos = Ensayos = 1000000

        ##################################################
        # Blocks
        ##################################################
        self.Menu = Qt.QTabWidget()
        self.Menu_widget_0 = Qt.QWidget()
        self.Menu_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Menu_widget_0)
        self.Menu_grid_layout_0 = Qt.QGridLayout()
        self.Menu_layout_0.addLayout(self.Menu_grid_layout_0)
        self.Menu.addTab(self.Menu_widget_0, 'banary random signal')
        self.top_grid_layout.addWidget(self.Menu, 1, 0, 1, 4)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        _run_stop_check_box = Qt.QCheckBox('Inicial/Parar')
        self._run_stop_choices = {True: True, False: False}
        self._run_stop_choices_inv = dict((v,k) for k,v in self._run_stop_choices.items())
        self._run_stop_callback = lambda i: Qt.QMetaObject.invokeMethod(_run_stop_check_box, "setChecked", Qt.Q_ARG("bool", self._run_stop_choices_inv[i]))
        self._run_stop_callback(self.run_stop)
        _run_stop_check_box.stateChanged.connect(lambda i: self.set_run_stop(self._run_stop_choices[bool(i)]))
        self.top_grid_layout.addWidget(_run_stop_check_box, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_vector_sink_f_0_1 = qtgui.vector_sink_f(
            N,
            -samp_rate/2,
            (samp_rate-1)/N,
            "Frecuencia",
            "Amplitud (Watt/Hz)",
            'PSD',
            1, # Number of inputs
            None # parent
        )
        self.qtgui_vector_sink_f_0_1.set_update_time(0.10)
        self.qtgui_vector_sink_f_0_1.set_y_axis(0., 1/Rb)
        self.qtgui_vector_sink_f_0_1.enable_autoscale(False)
        self.qtgui_vector_sink_f_0_1.enable_grid(False)
        self.qtgui_vector_sink_f_0_1.set_x_axis_units("Hz")
        self.qtgui_vector_sink_f_0_1.set_y_axis_units("Watt/Hz")
        self.qtgui_vector_sink_f_0_1.set_ref_level(0)

        labels = ['.', '', '', '', '',
            '', '', '', '', '']
        widths = [4, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_vector_sink_f_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_vector_sink_f_0_1.set_line_label(i, labels[i])
            self.qtgui_vector_sink_f_0_1.set_line_width(i, widths[i])
            self.qtgui_vector_sink_f_0_1.set_line_color(i, colors[i])
            self.qtgui_vector_sink_f_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_vector_sink_f_0_1_win = sip.wrapinstance(self.qtgui_vector_sink_f_0_1.pyqwidget(), Qt.QWidget)
        self.Menu_grid_layout_0.addWidget(self._qtgui_vector_sink_f_0_1_win, 2, 0, 1, 1)
        for r in range(2, 3):
            self.Menu_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.Menu_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_vector_sink_f_0 = qtgui.vector_sink_f(
            N,
            -(N/2)/samp_rate,
            (N/2)/samp_rate,
            "Rx(T)",
            "Amplitud",
            'Autocorrelacin',
            1, # Number of inputs
            None # parent
        )
        self.qtgui_vector_sink_f_0.set_update_time(0.10)
        self.qtgui_vector_sink_f_0.set_y_axis(-1, 2)
        self.qtgui_vector_sink_f_0.enable_autoscale(False)
        self.qtgui_vector_sink_f_0.enable_grid(False)
        self.qtgui_vector_sink_f_0.set_x_axis_units("T")
        self.qtgui_vector_sink_f_0.set_y_axis_units("Watt/Hz")
        self.qtgui_vector_sink_f_0.set_ref_level(0)

        labels = ['.', '', '', '', '',
            '', '', '', '', '']
        widths = [4, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_vector_sink_f_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_vector_sink_f_0.set_line_label(i, labels[i])
            self.qtgui_vector_sink_f_0.set_line_width(i, widths[i])
            self.qtgui_vector_sink_f_0.set_line_color(i, colors[i])
            self.qtgui_vector_sink_f_0.set_line_alpha(i, alphas[i])

        self._qtgui_vector_sink_f_0_win = sip.wrapinstance(self.qtgui_vector_sink_f_0.pyqwidget(), Qt.QWidget)
        self.Menu_grid_layout_0.addWidget(self._qtgui_vector_sink_f_0_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.Menu_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.Menu_grid_layout_0.setColumnStretch(c, 1)
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_fff(Sps, h)
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.fft_vxx_1 = fft.fft_vfc(N, True, window.rectangular(N), True, 1)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_float*1, N)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff(N*[1/samp_rate,])
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(N)
        self.b_binary_bipolar_source1_f_0 = b_binary_bipolar_source1_f(
            Am=1.,
        )
        _Mean_reset_push_button = Qt.QPushButton('Push here to restart averaging procces')
        _Mean_reset_push_button = Qt.QPushButton('Push here to restart averaging procces')
        self._Mean_reset_choices = {'Pressed': 0, 'Released': 1}
        _Mean_reset_push_button.pressed.connect(lambda: self.set_Mean_reset(self._Mean_reset_choices['Pressed']))
        _Mean_reset_push_button.released.connect(lambda: self.set_Mean_reset(self._Mean_reset_choices['Released']))
        self.top_grid_layout.addWidget(_Mean_reset_push_button, 0, 3, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(3, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.E3TRadio_vector_average_hob_0 = E3TRadio.vector_average_hob(N, Ensayos)
        self.E3TRadio_v_autocorr_ff_0 = E3TRadio.v_autocorr_ff(N)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.E3TRadio_v_autocorr_ff_0, 0), (self.E3TRadio_vector_average_hob_0, 0))
        self.connect((self.E3TRadio_vector_average_hob_0, 0), (self.fft_vxx_1, 0))
        self.connect((self.E3TRadio_vector_average_hob_0, 0), (self.qtgui_vector_sink_f_0, 0))
        self.connect((self.b_binary_bipolar_source1_f_0, 0), (self.interp_fir_filter_xxx_0, 0))
        self.connect((self.blocks_complex_to_mag_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_vector_sink_f_0_1, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.E3TRadio_v_autocorr_ff_0, 0))
        self.connect((self.fft_vxx_1, 0), (self.blocks_complex_to_mag_0, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.blocks_stream_to_vector_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_Rb(self.samp_rate/self.Sps)
        self.blocks_multiply_const_vxx_0.set_k(self.N*[1/self.samp_rate,])
        self.qtgui_vector_sink_f_0.set_x_axis(-(self.N/2)/self.samp_rate, (self.N/2)/self.samp_rate)
        self.qtgui_vector_sink_f_0_1.set_x_axis(-self.samp_rate/2, (self.samp_rate-1)/self.N)

    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps
        self.set_N(16*self.Sps)
        self.set_Rb(self.samp_rate/self.Sps)
        self.set_h(wform.rect(self.Sps))

    def get_run_stop(self):
        return self.run_stop

    def set_run_stop(self, run_stop):
        self.run_stop = run_stop
        if self.run_stop: self.start()
        else: self.stop(); self.wait()
        self._run_stop_callback(self.run_stop)

    def get_h(self):
        return self.h

    def set_h(self, h):
        self.h = h
        self.interp_fir_filter_xxx_0.set_taps(self.h)

    def get_Rb(self):
        return self.Rb

    def set_Rb(self, Rb):
        self.Rb = Rb
        self.qtgui_vector_sink_f_0_1.set_y_axis(0., 1/self.Rb)

    def get_N(self):
        return self.N

    def set_N(self, N):
        self.N = N
        self.blocks_multiply_const_vxx_0.set_k(self.N*[1/self.samp_rate,])
        self.qtgui_vector_sink_f_0.set_x_axis(-(self.N/2)/self.samp_rate, (self.N/2)/self.samp_rate)
        self.qtgui_vector_sink_f_0_1.set_x_axis(-self.samp_rate/2, (self.samp_rate-1)/self.N)

    def get_Mean_reset(self):
        return self.Mean_reset

    def set_Mean_reset(self, Mean_reset):
        self.Mean_reset = Mean_reset

    def get_Ensayos(self):
        return self.Ensayos

    def set_Ensayos(self, Ensayos):
        self.Ensayos = Ensayos




def main(top_block_cls=top_block, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
