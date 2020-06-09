'''
Created on Apr 21, 2020

@author: Daphne
'''

import os
import wx


# from wx.lib.agw import aui
# import wx.lib.splitter.MultiSplitterWindow


class OptionsControl(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.base_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.options_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.buttons_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.instructive_txt = wx.StaticText(self, label="Navigate by:")
        self.page_option = wx.CheckBox(self, label="Page", style=wx.ALIGN_RIGHT)
        self.panel_option = wx.CheckBox(self, label="Panel", style=wx.ALIGN_RIGHT)
        self.bubble_option = wx.CheckBox(self, label="Bubble", style=wx.ALIGN_RIGHT)

        self.previous_btn = wx.Button(self, label="Prev")
        self.next_btn = wx.Button(self, label="Next")

        self.options_sizer.AddMany([(self.instructive_txt, 0),
                                    (self.page_option, 0),
                                    (self.panel_option, 0),
                                    (self.bubble_option, 0)])

        self.buttons_sizer.AddMany([(self.previous_btn, 1), (self.next_btn, 1)])

        self.base_sizer.AddMany([(self.options_sizer, 2), (self.buttons_sizer, 1, wx.EXPAND)])

        self.SetSizer(self.base_sizer)


class NavigationControl(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.base_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.page_ctrl_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.panel_ctrl_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.bubble_ctrl_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # self.page_ctrl_sizer.Add(self.generic_ctrl_boilerplate("Page"), 0, wx.CENTER)

        self.base_sizer.AddMany([(self.generic_ctrl_boilerplate("Page"), 1),
                                 (self.generic_ctrl_boilerplate("Panel"), 1),
                                 (self.generic_ctrl_boilerplate("Bubble"), 1)])

        self.SetSizer(self.base_sizer)

    def generic_ctrl_boilerplate(self, label):
        ctrl_sizer = wx.BoxSizer(wx.HORIZONTAL)
        spin_label = wx.StaticText(self, label=label, style=wx.ALIGN_RIGHT)
        spin_ctrl = wx.SpinCtrl(self, wx.SP_WRAP | wx.SP_ARROW_KEYS)

        ctrl_sizer.Add(spin_label, 0)
        ctrl_sizer.Add(spin_ctrl, 0)

        return ctrl_sizer


class LabeledTextCtrl(wx.TextCtrl):
    def __init__(self, label, text_control_flags, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sizer = wx.StaticBoxSizer(wx.HORIZONTAL, self.GetParent(), label)
        self.sizer.Add(self, text_control_flags)


class AddOrEditVocabFrame(wx.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.base_panel = wx.Panel(self)
        self.add_vocab_sizer = wx.BoxSizer(wx.VERTICAL)
        self.add_btn_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.txt_ctrl_flags = wx.SizerFlags(1)

        self.save_btn = wx.Button(self.base_panel, label="Save")
        self.cancel_btn = wx.Button(self.base_panel, label="Cancel")

        self.vocab_txt = LabeledTextCtrl("Vocab", self.txt_ctrl_flags, self.base_panel)
        self.meaning_txt = LabeledTextCtrl("Meaning", self.txt_ctrl_flags, self.base_panel)
        self.sentence_txt = LabeledTextCtrl("Sentence(s)", self.txt_ctrl_flags, self.base_panel)
        self.notes_txt = LabeledTextCtrl("Notes", self.txt_ctrl_flags.Expand(), self.base_panel,
                                         style=wx.TE_MULTILINE | wx.VSCROLL)

        self.add_btn_sizer.AddMany([(self.save_btn, 0, wx.EXPAND), (wx.BoxSizer(wx.HORIZONTAL), 1, wx.EXPAND),
                                    (self.cancel_btn, 0, wx.EXPAND)])
        self.add_vocab_sizer.Add(self.add_btn_sizer, 0, wx.EXPAND)

        self.add_vocab_sizer.Add(self.vocab_txt.sizer, 0, wx.EXPAND)
        self.add_vocab_sizer.Add(self.meaning_txt.sizer, 0, wx.EXPAND)
        self.add_vocab_sizer.Add(self.sentence_txt.sizer, 0, wx.EXPAND)
        self.add_vocab_sizer.Add(self.notes_txt.sizer, 1, wx.EXPAND)

        self.base_panel.SetSizer(self.add_vocab_sizer)
        self.Show()

        self.save_btn.Bind(wx.EVT_BUTTON, self.on_save)
        self.cancel_btn.Bind(wx.EVT_BUTTON, self.on_cancel)

    def on_save(self, event):
        print("squawk save")

    def on_cancel(self, event):
        self.Destroy()


class DisplayVocabSection(wx.BoxSizer):
    def __init__(self, parent):
        super().__init__(wx.VERTICAL)
        self.parent = parent
        self.display_vocab_sizer = wx.BoxSizer(wx.VERTICAL)
        self.display_btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.display_vocab_wrapsizer = wx.WrapSizer(wx.HORIZONTAL)

        self.add_btn = wx.Button(self.parent, label="Add New")
        self.edit_btn = wx.Button(self.parent, label="Edit")
        self.remove_btn = wx.Button(self.parent, label="Remove")

        self.filter_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.filter_label = wx.StaticText(self.parent, label="Filter Vocab by ")
        self.filter_displayed_vocab = wx.Choice(self.parent, choices=["Bubble", "Panel", "Page", "All"],
                                                name="DisplayFilter")

        self.display_btn_sizer.AddMany([self.add_btn, self.edit_btn, self.remove_btn])
        self.filter_sizer.Add(self.filter_label, 0, wx.ALIGN_CENTER)
        self.filter_sizer.Add(self.filter_displayed_vocab, 0, wx.LEFT)
        self.filter_sizer.AddStretchSpacer(1)
        self.filter_sizer.Add(self.display_btn_sizer, 0, wx.RIGHT)
        self.Add(self.filter_sizer, 0, wx.EXPAND)

        # Pure placeholder below, this should be generated from save or added dynamically
        self.example_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.example_word = wx.Button(self.parent, label="HoverMe")
        self.example_word.SetToolTip("Vocab \nInfo")
        self.example_sizer.Add(self.example_word, 1, wx.EXPAND)
        self.display_vocab_wrapsizer.Add(self.example_sizer)
        # Pure placeholder above.

        self.Add(self.display_vocab_wrapsizer, wx.EXPAND)

        self.add_btn.Bind(wx.EVT_BUTTON, self.on_add_or_edit)
        self.edit_btn.Bind(wx.EVT_BUTTON, self.on_add_or_edit)

    def on_add_or_edit(self, event):
        AddOrEditVocabFrame(self.parent)


class BubbleOverview(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.base_sizer = wx.BoxSizer(wx.VERTICAL)

        self.txt_ctrl_flags = wx.SizerFlags(1)

        self.bubble_translation_txt = LabeledTextCtrl("Full Translation", self.txt_ctrl_flags.Expand(),
                                                      self, style=wx.TE_MULTILINE | wx.VSCROLL)
        self.bubble_notes_txt = LabeledTextCtrl("Translation Notes", self.txt_ctrl_flags.Expand(), self,
                                                style=wx.TE_MULTILINE | wx.VSCROLL)

        self.base_sizer.Add(self.bubble_translation_txt.sizer, 1, wx.EXPAND)
        self.base_sizer.Add(self.bubble_notes_txt.sizer, 1, wx.EXPAND)

        self.SetSizer(self.base_sizer)


class PanelOverview(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.base_sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.base_sizer)


class PageOverview(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.base_sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.base_sizer)


class TranslationTreebook(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        self.treebook = wx.Treebook(self)
        self.treebook_control = self.treebook.GetTreeCtrl()

        self.base_sizer = wx.BoxSizer(wx.VERTICAL)

        self.page_overview_panel = PageOverview(self.treebook)
        self.panel_overview_panel = PanelOverview(self.treebook)
        self.bubble_overview_panel = BubbleOverview(self.treebook)

        self.treebook.AddPage(self.page_overview_panel, "Page 1")
        self.treebook.AddSubPage(self.panel_overview_panel, "Panel 1")
        self.treebook.InsertSubPage(1, self.bubble_overview_panel, "Bubble 300")

        self.treebook_control.SetMinSize([125,
                                          self.treebook_control.GetMinSize().height])  # forces control to be wide enough to display fully expanded tree

        self.base_sizer.Add(self.treebook, 1, wx.EXPAND)
        self.SetSizer(self.base_sizer)


class Test(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Notes')
        self.splitter = wx.SplitterWindow(self, style=wx.SP_NO_XP_THEME | wx.SP_3D | wx.SP_LIVE_UPDATE)

        self.top_panel = wx.Panel(self.splitter)
        self.bottom_panel = wx.Panel(self.splitter)

        self.vocab_panel = DisplayVocabSection(self.top_panel)
        self.notes_panel = TranslationTreebook(self.bottom_panel)
        self.options_panel = OptionsControl(self.bottom_panel)
        self.navigation_panel = NavigationControl(self.bottom_panel)

        self.splitter_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.top_sizer = wx.BoxSizer(wx.VERTICAL)
        self.bottom_sizer = wx.BoxSizer(wx.VERTICAL)

        self.splitter_sizer.Add(self.splitter, 1, wx.EXPAND)
        self.top_sizer.Add(self.vocab_panel, 1, wx.EXPAND)
        self.bottom_sizer.Add(self.options_panel, 0, wx.EXPAND)
        self.bottom_sizer.Add(self.notes_panel, 1, wx.EXPAND)
        self.bottom_sizer.Add(self.navigation_panel, 0, wx.CENTER)

        self.top_panel.SetSizerAndFit(self.vocab_panel)
        self.bottom_panel.SetSizerAndFit(self.bottom_sizer)

        self.splitter.SplitHorizontally(self.top_panel, self.bottom_panel)
        # self.splitter.SetMinimumPaneSize(self.vocab_panel.GetPage(1).GetMinSize().y)

        self.SetSizerAndFit(self.splitter_sizer)
        self.Show()


if __name__ == '__main__':
    app = wx.App()
    window = Test()
    app.MainLoop()
