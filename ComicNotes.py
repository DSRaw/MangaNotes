'''
Created on Apr 21, 2020

@author: Daphne
'''

import os
import wx

class LabeledTextCtrl(wx.TextCtrl):
    def __init__(self, label, text_control_flags, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sizer = wx.StaticBoxSizer(wx.HORIZONTAL, self.GetParent(), label)
        self.sizer.Add(self, text_control_flags)

    def SetBadge(self, badge):
        self.sizer.label = "foo"

class Test(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Notes')

        self.notebook = wx.Notebook(self)
        self.base_panel = wx.Panel(self.notebook)

        self.base_sizer = wx.BoxSizer(wx.VERTICAL)
        self.vocab_sizer = wx.BoxSizer(wx.VERTICAL)
        self.notes_sizer = wx.BoxSizer(wx.VERTICAL)

        self.txt_ctrl_flags = wx.SizerFlags(1)

        #In Vocab Sizer:
        self.vocab_txt = LabeledTextCtrl("Vocab", self.txt_ctrl_flags, self.base_panel)
        self.meaning_txt = LabeledTextCtrl("Meaning", self.txt_ctrl_flags, self.base_panel)
        self.sentence_txt = LabeledTextCtrl("Sentence(s)", self.txt_ctrl_flags, self.base_panel)
        self.notes_txt = LabeledTextCtrl("Notes", self.txt_ctrl_flags.Expand(), self.base_panel, style=wx.TE_MULTILINE | wx.VSCROLL)

        self.vocab_sizer.Add(self.vocab_txt.sizer, 0, wx.EXPAND)
        self.vocab_sizer.Add(self.meaning_txt.sizer, 0, wx.EXPAND)
        self.vocab_sizer.Add(self.sentence_txt.sizer, 0, wx.EXPAND)
        self.vocab_sizer.Add(self.notes_txt.sizer, 1, wx.EXPAND)

        # In Notes Sizer:
        self.bubble_translation_txt = LabeledTextCtrl("Full Translation", self.txt_ctrl_flags.Expand(), self.base_panel, style=wx.TE_MULTILINE | wx.VSCROLL)
        self.bubble_notes_txt = LabeledTextCtrl("Translation Notes", self.txt_ctrl_flags.Expand(), self.base_panel, style=wx.TE_MULTILINE | wx.VSCROLL)

        self.notes_sizer.Add(self.bubble_translation_txt.sizer, 1, wx.EXPAND)
        self.notes_sizer.Add(self.bubble_notes_txt.sizer, 1, wx.EXPAND)

        #Add all to Base Sizer:
        self.base_sizer.Add(self.vocab_sizer, 1, wx.EXPAND)
        self.base_sizer.Add(self.notes_sizer, 2, wx.EXPAND)

        self.base_panel.SetSizerAndFit(self.base_sizer)

        self.notebook.AddPage(self.base_panel, "Bubble 1", True)

        self.SetSizeHints(self.base_panel.GetMinSize())
        
        self.Show()
    
if __name__ == '__main__':
    app = wx.App()
    window = Test()
    app.MainLoop()
