import maya.cmds as cmds
from ChangeWireframeColor import wireframeColor

class WireframeColorUI():
    def __init__(self):
        self.window_name = 'WireframeColor'

    def delete(self):
        if cmds.window(self.window_name, exists=True):
            cmds.deleteUI(self.window_name)

    def create(self):
        self.delete()

        self.window_name = cmds.window(self.window_name, title='%s Tool' % self.window_name, widthHeight=(500, 100))
        self.columnlayout()
        cmds.showWindow(self.window_name)

    def columnlayout(self):
        cmds.columnLayout(adjustableColumn=True)
        self.color_slider = cmds.intSliderGrp(label='Wireframe Color', field=True, minValue=0, maxValue=31, value=0)
        self.apply_button = cmds.button(label='Apply', command=self.on_button_click)

    def on_button_click(self, *args):
        color = cmds.intSliderGrp(self.color_slider, query=True, value=True)
        wireframeColor(color)

ui = WireframeColorUI()
ui.create()