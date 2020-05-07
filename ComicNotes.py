'''
Created on Apr 21, 2020

@author: Daphne
'''

import os
import wx
#from wx.lib.agw import aui
#import wx.lib.splitter.MultiSplitterWindow

'''
class NoteFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='NoteFrame')
        self.baseSizer = wx.BoxSizer(wx.VERTICAL)
        
        self.buttonsSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.buttonsPanel = wx.Panel(self, style=wx.BORDER_RAISED)
        
        self.btnAddVertical = wx.Button(self.buttonsPanel, label="+ VSection")
        self.btnAddHorizontal = wx.Button(self.buttonsPanel, label="+ HSection")
        
        self.Bind(wx.EVT_BUTTON, self.add_vertical_section, self.btnAddVertical)
        self.Bind(wx.EVT_BUTTON, self.add_horizontal_section, self.btnAddHorizontal)
        
        self.splitter = wx.SplitterWindow(self, style=wx.SP_NO_XP_THEME | wx.SP_3DSASH | wx.SP_LIVE_UPDATE)
        self.splitter.SetSashGravity(0.5)
        
        #initPanel = wx.Panel(self.splitter)
        #self.splitter.Initialize(initPanel)
        #twoPanel = wx.Panel(self.splitter)
        
        #self.splitter.SplitHorizontally(onePanel, twoPanel)
        #self.splitter.SplitHorizontally(onePanel, twoPanel)
        
        
        self.buttonsSizer.Add(self.btnAddVertical)
        self.buttonsSizer.Add(self.btnAddHorizontal)
        self.buttonsPanel.SetSizer(self.buttonsSizer)
        
        self.baseSizer.Add(self.buttonsPanel, 0, wx.ALIGN_TOP | wx.EXPAND)
        self.baseSizer.Add(self.splitter, 1,  wx.EXPAND)
        
        self.SetSizer(self.baseSizer)
        self.Show()
        
    def new_page(self):
        pass
     
    def add_vertical_section(self, event):
        print("vert")
        leftPanel = wx.Panel(self.splitter)
        rightPanel = wx.Panel(self.splitter)
        self.splitter.SplitVertically(leftPanel, rightPanel)
        
    def add_horizontal_section(self, event):
        print("hori")
        self.newSplitterSizer = wx.BoxSizer(wx.VERTICAL)
        self.newSplitter = wx.SplitterWindow(self, style=wx.SP_NO_XP_THEME | wx.SP_3DSASH | wx.SP_LIVE_UPDATE)
        self.newSplitter.SetSashGravity(0.5)
        
        topPanel = wx.Panel(self.newSplitter)      #Will need to just copy the window into a new one. Also need to initialize OG splitter with 1 window
        bottomPanel = wx.Panel(self.newSplitter)
        
        
        self.newSplitter.SplitHorizontally(topPanel, bottomPanel)
        self.newSplitterSizer.Add(self.newSplitter)
        
        #topPanel = wx.Panel(self.splitter)
        #bottomPanel = wx.Panel(self.splitter)
        #self.splitter.SplitHorizontally(topPanel, bottomPanel)
        
        self.splitter.ReplaceWindow(self.splitter.GetWindow1(), self.newSplitter)
        
    def new_subsec(self):
        pass
    
class Test2(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='NoteFrame')
        self.baseSizer = wx.BoxSizer(wx.VERTICAL)
        self.buttonSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.buttonsPanel = wx.Panel(self, style=wx.BORDER_RAISED)
        
        self.btnAddVertical = wx.Button(self.buttonsPanel, label="+ VSection")
        self.btnAddHorizontal = wx.Button(self.buttonsPanel, label="+ HSection")
        
        self.Bind(wx.EVT_BUTTON, self.add_vertical_section, self.btnAddVertical)
        self.Bind(wx.EVT_BUTTON, self.add_horizontal_section, self.btnAddHorizontal)
        
        #self.splitter = wx.lib.splitter.MultiSplitterWindow
        
        self.buttonSizer.Add(self.btnAddVertical)
        self.buttonSizer.Add(self.btnAddHorizontal)
        self.buttonsPanel.SetSizer(self.buttonSizer)
        
        self.baseSizer.Add(self.buttonsPanel, 0, wx.ALIGN_TOP | wx.EXPAND)
        self.baseSizer.Add(self.splitter, 1,  wx.EXPAND)
        
        self.SetSizer(self.baseSizer)
        self.Show()
        
    def add_vertical_section(self, event):
        pass
        
    def add_horizontal_section(self, event):
        pass

'''
'''
class Test2(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='NoteFrame')
    
        self.mgr = aui.AuiManager(self, aui.AUI_MGR_DEFAULT)
        #self.mgr.SetManagedWindow(self)
        
        text1 = wx.TextCtrl(self)
        text2 = wx.TextCtrl(self)

        panel1 = wx.Panel(self)
        #put both of the following inside an outter pane
        self.mgr.AddPane(panel1, wx.CENTER, "Root")
        self.mgr.AddPane(text1, wx.RIGHT, "Pane 1")
        self.mgr.AddPane(text2, wx.RIGHT, "Pane 2")

        
        ''''''
        self.panel = wx.Panel(self, style=wx.BORDER_SIMPLE)
        self.panel_info = aui.AuiPaneInfo().Right()
        
        self.panel2 = wx.Panel(self, style=wx.BORDER_SIMPLE)
        self.panel_info2 = aui.AuiPaneInfo().Left()
        
        self.mgr.AddPane(self.panel, self.panel_info)
        self.mgr.AddPane(self.panel2, self.panel_info2)
        ''''''

        self.mgr.Update()
        self.Show()
        
    
    def __OnQuit(self, event):
        self.mgr.UnInit()
        del self.mgr
        self.Destroy()
        '''

class LabeledTextCtrl(wx.TextCtrl):
    def __init__(self, label, text_control_flags, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.ctrl_label = wx.StaticText(self.GetParent())
        self.sizer = wx.StaticBoxSizer(wx.HORIZONTAL, self.GetParent(), label)
        #self.sizer.Add(self.ctrl_label, 0, wx.LEFT)
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

        print(self.base_sizer.GetMinSize())
        #self.mgr = aui.AuiManager(self, aui.AUI_MGR_DEFAULT)
        #self.mgr.AddPane(self, wx.RIGHT, "Pane 2")
        #self.mgr.Update()

        self.SetSizeHints(self.base_panel.GetMinSize())
        self.Show()
        print(self.GetSize())
    
if __name__ == '__main__':
    app = wx.App()
    window = Test()
    app.MainLoop()