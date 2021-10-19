#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.4),
    on Thu Sep 10 12:50:52 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.4'
expName = 'effortful_help'  # from the Builder filename that created this script
expInfo = {'participant': '', 'gender': ['1: male', '0: female'], 'age': '', 'session': '001', 'Alipay(支付宝账户)': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sort_keys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data' + os.sep + '%s_%s' % (expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/sylviacao/Desktop/eff-alt-01/effortful_help.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='norm')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instrMessage = visual.TextStim(win=win, name='instrMessage',
    text='您好，欢迎参加实验！ 实验共有两轮，你会与1名其他参与者共同完成实验。 每轮实验您将会被分配到一种角色：1）助人者；2）求助者。  请按空格键[space]继续',
    font='simkai',
    pos=[0, 0], height=0.06, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
resp = keyboard.Keyboard()
name_list = ['liqiyu', 'xiaomingcheng', 'quanyuwen']
nameShow = name_list[int(random()*len(name_list))]

# Initialize components for Routine "roleAssign"
roleAssignClock = core.Clock()
instr_role = visual.TextStim(win=win, name='instr_role',
    text='理解后，请按空格键[space]继续 ',
    font='Arial',
    pos=(0, -0.6), height=0.06, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_1 = keyboard.Keyboard()
role_assign = visual.ImageStim(
    win=win,
    name='role_assign', 
    image='instru_role.png', mask=None,
    ori=0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)

# Initialize components for Routine "rewardExplain"
rewardExplainClock = core.Clock()
instr_reward = visual.TextStim(win=win, name='instr_reward',
    text='您可以根据自己的意愿帮助他人减少损失 理解后，请按空格键[space]继续 ',
    font='Arial',
    pos=(0, -0.6), height=0.06, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()
reward_explain = visual.ImageStim(
    win=win,
    name='reward_explain', 
    image='reward_explain.png', mask=None,
    ori=0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
tiral_cue = visual.ImageStim(
    win=win,
    name='tiral_cue', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)

# Initialize components for Routine "waiting"
waitingClock = core.Clock()
waitText = visual.TextStim(win=win, name='waitText',
    text='请您耐心等待另外一名玩家2s小游戏 您将会看到根据ta的任务表现计算的损失水平',
    font='simsun',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
countdown_2s = visual.TextStim(win=win, name='countdown_2s',
    text='请等待 2s',
    font='Arial',
    pos=(0, -0.3), height=0.1, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
countdown_1s = visual.TextStim(win=win, name='countdown_1s',
    text='请等待 1s',
    font='Arial',
    pos=(0, -0.3), height=0.1, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
waitForOutcome = visual.TextStim(win=win, name='waitForOutcome',
    text='请等待结果计算…',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "loss_level"
loss_levelClock = core.Clock()
name = visual.TextStim(win=win, name='name',
    text='default text',
    font='Arial',
    pos=(0, 0.6), height=0.1, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
loss_level1 = visual.Rect(
    win=win, name='loss_level1',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0.5, depth=-2.0, interpolate=True)
loss_level2 = visual.Rect(
    win=win, name='loss_level2',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-0.765,0.129,1.000], fillColorSpace='rgb',
    opacity=0.5, depth=-3.0, interpolate=True)
loss_level3 = visual.Rect(
    win=win, name='loss_level3',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0.867,-0.655,-0.655], fillColorSpace='rgb',
    opacity=0.5, depth=-4.0, interpolate=True)

# Initialize components for Routine "EffortTask"
EffortTaskClock = core.Clock()
skey_resp = keyboard.Keyboard()
balloonSize=0.08
balloonMsgHeight=0.01
balloonBody = visual.ImageStim(
    win=win,
    name='balloonBody', 
    image='redBalloon.png', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
reminderMsg = visual.TextStim(win=win, name='reminderMsg',
    text='请按空格键 [space]将气球充气',
    font='Arial',
    pos=[0, -0.8], height=0.05, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
balloonValMsg = visual.TextStim(win=win, name='balloonValMsg',
    text='为了帮助他人减少损失： 请您在3s内尽可能的将气球充气打！ 任务失败则没有办法帮助他人',
    font='Arial',
    pos=[0,0.05], height=0.06, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "effort_evaluation"
effort_evaluationClock = core.Clock()
instr_evaluation = visual.TextStim(win=win, name='instr_evaluation',
    text="请您评价自己在气球任务中的努力程度 请点击‘Q'键表示“确定”",
    font='Arial',
    pos=(0, 0.4), height=0.08, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
slider = visual.Slider(win=win, name='slider',
    size=(1.0, 0.1), pos=(0, -0.3), units=None,
    labels=['0%', '100%'], ticks=[0, 1],
    granularity=0, style=['rating'],
    color='LightGray', font='HelveticaBold',
    flip=False)
evaluation_show = visual.TextStim(win=win, name='evaluation_show',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
ok_confirmation = keyboard.Keyboard()

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
feedback = '恭喜!您成功帮助了对方玩家'
feedbackMsg = visual.TextStim(win=win, name='feedbackMsg',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "final"
finalClock = core.Clock()
final_bank = visual.TextStim(win=win, name='final_bank',
    text='您的账户已存入15元 在您实验后1-2天内，主试会将您的被试费打入您的账户。请按空格键[space]退出',
    font='Arial',
    pos=[0, 0], height=0.08, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
doneKey = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions"-------
continueRoutine = True
# update component parameters for each repeat
resp.keys = []
resp.rt = []
_resp_allKeys = []
# keep track of which components have finished
instructionsComponents = [instrMessage, resp]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instrMessage* updates
    if instrMessage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instrMessage.frameNStart = frameN  # exact frame index
        instrMessage.tStart = t  # local t and not account for scr refresh
        instrMessage.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrMessage, 'tStartRefresh')  # time at next scr refresh
        instrMessage.setAutoDraw(True)
    
    # *resp* updates
    waitOnFlip = False
    if resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        resp.frameNStart = frameN  # exact frame index
        resp.tStart = t  # local t and not account for scr refresh
        resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
        resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if resp.status == STARTED and not waitOnFlip:
        theseKeys = resp.getKeys(keyList=['space'], waitRelease=False)
        _resp_allKeys.extend(theseKeys)
        if len(_resp_allKeys):
            resp.keys = _resp_allKeys[-1].name  # just the last key pressed
            resp.rt = _resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instrMessage.started', instrMessage.tStartRefresh)
thisExp.addData('instrMessage.stopped', instrMessage.tStopRefresh)
# check responses
if resp.keys in ['', [], None]:  # No response was made
    resp.keys = None
thisExp.addData('resp.keys',resp.keys)
if resp.keys != None:  # we had a response
    thisExp.addData('resp.rt', resp.rt)
thisExp.addData('resp.started', resp.tStartRefresh)
thisExp.addData('resp.stopped', resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "roleAssign"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_1.keys = []
key_resp_1.rt = []
_key_resp_1_allKeys = []
# keep track of which components have finished
roleAssignComponents = [instr_role, key_resp_1, role_assign]
for thisComponent in roleAssignComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
roleAssignClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "roleAssign"-------
while continueRoutine:
    # get current time
    t = roleAssignClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=roleAssignClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_role* updates
    if instr_role.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_role.frameNStart = frameN  # exact frame index
        instr_role.tStart = t  # local t and not account for scr refresh
        instr_role.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_role, 'tStartRefresh')  # time at next scr refresh
        instr_role.setAutoDraw(True)
    
    # *key_resp_1* updates
    waitOnFlip = False
    if key_resp_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_1.frameNStart = frameN  # exact frame index
        key_resp_1.tStart = t  # local t and not account for scr refresh
        key_resp_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_1, 'tStartRefresh')  # time at next scr refresh
        key_resp_1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_1.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_1.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_1_allKeys.extend(theseKeys)
        if len(_key_resp_1_allKeys):
            key_resp_1.keys = _key_resp_1_allKeys[-1].name  # just the last key pressed
            key_resp_1.rt = _key_resp_1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *role_assign* updates
    if role_assign.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        role_assign.frameNStart = frameN  # exact frame index
        role_assign.tStart = t  # local t and not account for scr refresh
        role_assign.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(role_assign, 'tStartRefresh')  # time at next scr refresh
        role_assign.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in roleAssignComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "roleAssign"-------
for thisComponent in roleAssignComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr_role.started', instr_role.tStartRefresh)
thisExp.addData('instr_role.stopped', instr_role.tStopRefresh)
# check responses
if key_resp_1.keys in ['', [], None]:  # No response was made
    key_resp_1.keys = None
thisExp.addData('key_resp_1.keys',key_resp_1.keys)
if key_resp_1.keys != None:  # we had a response
    thisExp.addData('key_resp_1.rt', key_resp_1.rt)
thisExp.addData('key_resp_1.started', key_resp_1.tStartRefresh)
thisExp.addData('key_resp_1.stopped', key_resp_1.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('role_assign.started', role_assign.tStartRefresh)
thisExp.addData('role_assign.stopped', role_assign.tStopRefresh)
# the Routine "roleAssign" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "rewardExplain"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
rewardExplainComponents = [instr_reward, key_resp_2, reward_explain]
for thisComponent in rewardExplainComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
rewardExplainClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "rewardExplain"-------
while continueRoutine:
    # get current time
    t = rewardExplainClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=rewardExplainClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_reward* updates
    if instr_reward.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_reward.frameNStart = frameN  # exact frame index
        instr_reward.tStart = t  # local t and not account for scr refresh
        instr_reward.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_reward, 'tStartRefresh')  # time at next scr refresh
        instr_reward.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *reward_explain* updates
    if reward_explain.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        reward_explain.frameNStart = frameN  # exact frame index
        reward_explain.tStart = t  # local t and not account for scr refresh
        reward_explain.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(reward_explain, 'tStartRefresh')  # time at next scr refresh
        reward_explain.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in rewardExplainComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "rewardExplain"-------
for thisComponent in rewardExplainComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr_reward.started', instr_reward.tStartRefresh)
thisExp.addData('instr_reward.stopped', instr_reward.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('reward_explain.started', reward_explain.tStartRefresh)
thisExp.addData('reward_explain.stopped', reward_explain.tStopRefresh)
# the Routine "rewardExplain" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialTypes_effort.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fixation"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if pay_type < 1:
        fixationPic = 'nonself_pay.png'
    else:
        fixationPic = 'self_pay.png'
        
    
    tiral_cue.setImage(fixationPic)
    # keep track of which components have finished
    fixationComponents = [tiral_cue]
    for thisComponent in fixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fixation"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *tiral_cue* updates
        if tiral_cue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            tiral_cue.frameNStart = frameN  # exact frame index
            tiral_cue.tStart = t  # local t and not account for scr refresh
            tiral_cue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tiral_cue, 'tStartRefresh')  # time at next scr refresh
            tiral_cue.setAutoDraw(True)
        if tiral_cue.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > tiral_cue.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                tiral_cue.tStop = t  # not accounting for scr refresh
                tiral_cue.frameNStop = frameN  # exact frame index
                win.timeOnFlip(tiral_cue, 'tStopRefresh')  # time at next scr refresh
                tiral_cue.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixation"-------
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('tiral_cue.started', tiral_cue.tStartRefresh)
    trials.addData('tiral_cue.stopped', tiral_cue.tStopRefresh)
    
    # ------Prepare to start Routine "waiting"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    waitingComponents = [waitText, countdown_2s, countdown_1s, waitForOutcome]
    for thisComponent in waitingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    waitingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "waiting"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = waitingClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=waitingClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *waitText* updates
        if waitText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            waitText.frameNStart = frameN  # exact frame index
            waitText.tStart = t  # local t and not account for scr refresh
            waitText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(waitText, 'tStartRefresh')  # time at next scr refresh
            waitText.setAutoDraw(True)
        if waitText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > waitText.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                waitText.tStop = t  # not accounting for scr refresh
                waitText.frameNStop = frameN  # exact frame index
                win.timeOnFlip(waitText, 'tStopRefresh')  # time at next scr refresh
                waitText.setAutoDraw(False)
        
        # *countdown_2s* updates
        if countdown_2s.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            countdown_2s.frameNStart = frameN  # exact frame index
            countdown_2s.tStart = t  # local t and not account for scr refresh
            countdown_2s.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(countdown_2s, 'tStartRefresh')  # time at next scr refresh
            countdown_2s.setAutoDraw(True)
        if countdown_2s.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > countdown_2s.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                countdown_2s.tStop = t  # not accounting for scr refresh
                countdown_2s.frameNStop = frameN  # exact frame index
                win.timeOnFlip(countdown_2s, 'tStopRefresh')  # time at next scr refresh
                countdown_2s.setAutoDraw(False)
        
        # *countdown_1s* updates
        if countdown_1s.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            countdown_1s.frameNStart = frameN  # exact frame index
            countdown_1s.tStart = t  # local t and not account for scr refresh
            countdown_1s.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(countdown_1s, 'tStartRefresh')  # time at next scr refresh
            countdown_1s.setAutoDraw(True)
        if countdown_1s.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > countdown_1s.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                countdown_1s.tStop = t  # not accounting for scr refresh
                countdown_1s.frameNStop = frameN  # exact frame index
                win.timeOnFlip(countdown_1s, 'tStopRefresh')  # time at next scr refresh
                countdown_1s.setAutoDraw(False)
        
        # *waitForOutcome* updates
        if waitForOutcome.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            waitForOutcome.frameNStart = frameN  # exact frame index
            waitForOutcome.tStart = t  # local t and not account for scr refresh
            waitForOutcome.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(waitForOutcome, 'tStartRefresh')  # time at next scr refresh
            waitForOutcome.setAutoDraw(True)
        if waitForOutcome.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > waitForOutcome.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                waitForOutcome.tStop = t  # not accounting for scr refresh
                waitForOutcome.frameNStop = frameN  # exact frame index
                win.timeOnFlip(waitForOutcome, 'tStopRefresh')  # time at next scr refresh
                waitForOutcome.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in waitingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "waiting"-------
    for thisComponent in waitingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('waitText.started', waitText.tStartRefresh)
    trials.addData('waitText.stopped', waitText.tStopRefresh)
    trials.addData('countdown_2s.started', countdown_2s.tStartRefresh)
    trials.addData('countdown_2s.stopped', countdown_2s.tStopRefresh)
    trials.addData('countdown_1s.started', countdown_1s.tStartRefresh)
    trials.addData('countdown_1s.stopped', countdown_1s.tStopRefresh)
    trials.addData('waitForOutcome.started', waitForOutcome.tStartRefresh)
    trials.addData('waitForOutcome.stopped', waitForOutcome.tStopRefresh)
    
    # ------Prepare to start Routine "loss_level"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    nameShow_loss = nameShow + "的损失水平为"
    
    pos1 = 0
    pos2 = 0
    pos3 = 0
    if opac_1<0.1:
        pos1 =[5, 5]
    else:
        pos1 = (0, -0.2)
    
    if opac_2<0.1:
        pos2 =[5, 5]
    else:
        pos2 = (0, 0)
    
    if opac_3<0.1:
        pos3 =[5, 5]
    else:
        pos3 = (0, 0.2)
    
    print(pos1, pos2, pos3)
    name.setText(nameShow_loss)
    loss_level1.setPos([pos1[0],pos1[1]])
    loss_level2.setPos([pos2[0],pos2[1]])
    loss_level3.setPos([pos3[0],pos3[1]])
    # keep track of which components have finished
    loss_levelComponents = [name, loss_level1, loss_level2, loss_level3]
    for thisComponent in loss_levelComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    loss_levelClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "loss_level"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = loss_levelClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=loss_levelClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *name* updates
        if name.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            name.frameNStart = frameN  # exact frame index
            name.tStart = t  # local t and not account for scr refresh
            name.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(name, 'tStartRefresh')  # time at next scr refresh
            name.setAutoDraw(True)
        if name.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > name.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                name.tStop = t  # not accounting for scr refresh
                name.frameNStop = frameN  # exact frame index
                win.timeOnFlip(name, 'tStopRefresh')  # time at next scr refresh
                name.setAutoDraw(False)
        
        # *loss_level1* updates
        if loss_level1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            loss_level1.frameNStart = frameN  # exact frame index
            loss_level1.tStart = t  # local t and not account for scr refresh
            loss_level1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(loss_level1, 'tStartRefresh')  # time at next scr refresh
            loss_level1.setAutoDraw(True)
        if loss_level1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > loss_level1.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                loss_level1.tStop = t  # not accounting for scr refresh
                loss_level1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(loss_level1, 'tStopRefresh')  # time at next scr refresh
                loss_level1.setAutoDraw(False)
        
        # *loss_level2* updates
        if loss_level2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            loss_level2.frameNStart = frameN  # exact frame index
            loss_level2.tStart = t  # local t and not account for scr refresh
            loss_level2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(loss_level2, 'tStartRefresh')  # time at next scr refresh
            loss_level2.setAutoDraw(True)
        if loss_level2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > loss_level2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                loss_level2.tStop = t  # not accounting for scr refresh
                loss_level2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(loss_level2, 'tStopRefresh')  # time at next scr refresh
                loss_level2.setAutoDraw(False)
        
        # *loss_level3* updates
        if loss_level3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            loss_level3.frameNStart = frameN  # exact frame index
            loss_level3.tStart = t  # local t and not account for scr refresh
            loss_level3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(loss_level3, 'tStartRefresh')  # time at next scr refresh
            loss_level3.setAutoDraw(True)
        if loss_level3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > loss_level3.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                loss_level3.tStop = t  # not accounting for scr refresh
                loss_level3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(loss_level3, 'tStopRefresh')  # time at next scr refresh
                loss_level3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in loss_levelComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "loss_level"-------
    for thisComponent in loss_levelComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('name.started', name.tStartRefresh)
    trials.addData('name.stopped', name.tStopRefresh)
    trials.addData('loss_level1.started', loss_level1.tStartRefresh)
    trials.addData('loss_level1.stopped', loss_level1.tStopRefresh)
    trials.addData('loss_level2.started', loss_level2.tStartRefresh)
    trials.addData('loss_level2.stopped', loss_level2.tStopRefresh)
    trials.addData('loss_level3.started', loss_level3.tStartRefresh)
    trials.addData('loss_level3.stopped', loss_level3.tStopRefresh)
    
    # ------Prepare to start Routine "EffortTask"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    skey_resp.keys = []
    skey_resp.rt = []
    _skey_resp_allKeys = []
    balloonSize=0.08
    popped=False
    nPumps=0
    print('start')
    # keep track of which components have finished
    EffortTaskComponents = [skey_resp, balloonBody, reminderMsg, balloonValMsg]
    for thisComponent in EffortTaskComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    EffortTaskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "EffortTask"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = EffortTaskClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=EffortTaskClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *skey_resp* updates
        waitOnFlip = False
        if skey_resp.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            skey_resp.frameNStart = frameN  # exact frame index
            skey_resp.tStart = t  # local t and not account for scr refresh
            skey_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(skey_resp, 'tStartRefresh')  # time at next scr refresh
            skey_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(skey_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(skey_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if skey_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > skey_resp.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                skey_resp.tStop = t  # not accounting for scr refresh
                skey_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(skey_resp, 'tStopRefresh')  # time at next scr refresh
                skey_resp.status = FINISHED
        if skey_resp.status == STARTED and not waitOnFlip:
            theseKeys = skey_resp.getKeys(keyList=['space'], waitRelease=False)
            _skey_resp_allKeys.extend(theseKeys)
            if len(_skey_resp_allKeys):
                skey_resp.keys = [key.name for key in _skey_resp_allKeys]  # storing all keys
                skey_resp.rt = [key.rt for key in _skey_resp_allKeys]
        balloonSize=0.1+nPumps*0.015
        
        # *balloonBody* updates
        if balloonBody.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            balloonBody.frameNStart = frameN  # exact frame index
            balloonBody.tStart = t  # local t and not account for scr refresh
            balloonBody.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(balloonBody, 'tStartRefresh')  # time at next scr refresh
            balloonBody.setAutoDraw(True)
        if balloonBody.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > balloonBody.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                balloonBody.tStop = t  # not accounting for scr refresh
                balloonBody.frameNStop = frameN  # exact frame index
                win.timeOnFlip(balloonBody, 'tStopRefresh')  # time at next scr refresh
                balloonBody.setAutoDraw(False)
        if balloonBody.status == STARTED:  # only update if drawing
            balloonBody.setPos([-1+balloonSize/2, 0], log=False)
            balloonBody.setSize(balloonSize, log=False)
        
        # *reminderMsg* updates
        if reminderMsg.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            reminderMsg.frameNStart = frameN  # exact frame index
            reminderMsg.tStart = t  # local t and not account for scr refresh
            reminderMsg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(reminderMsg, 'tStartRefresh')  # time at next scr refresh
            reminderMsg.setAutoDraw(True)
        if reminderMsg.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > reminderMsg.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                reminderMsg.tStop = t  # not accounting for scr refresh
                reminderMsg.frameNStop = frameN  # exact frame index
                win.timeOnFlip(reminderMsg, 'tStopRefresh')  # time at next scr refresh
                reminderMsg.setAutoDraw(False)
        
        # *balloonValMsg* updates
        if balloonValMsg.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            balloonValMsg.frameNStart = frameN  # exact frame index
            balloonValMsg.tStart = t  # local t and not account for scr refresh
            balloonValMsg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(balloonValMsg, 'tStartRefresh')  # time at next scr refresh
            balloonValMsg.setAutoDraw(True)
        if balloonValMsg.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > balloonValMsg.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                balloonValMsg.tStop = t  # not accounting for scr refresh
                balloonValMsg.frameNStop = frameN  # exact frame index
                win.timeOnFlip(balloonValMsg, 'tStopRefresh')  # time at next scr refresh
                balloonValMsg.setAutoDraw(False)
        if skey_resp.keys:
          nPumps = len(skey_resp.keys)
          
        print(nPumps)
        #  if nPumps>maxPumps:
        #    popped=True
        #    continueRoutine=False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EffortTaskComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "EffortTask"-------
    for thisComponent in EffortTaskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if skey_resp.keys in ['', [], None]:  # No response was made
        skey_resp.keys = None
    trials.addData('skey_resp.keys',skey_resp.keys)
    if skey_resp.keys != None:  # we had a response
        trials.addData('skey_resp.rt', skey_resp.rt)
    trials.addData('skey_resp.started', skey_resp.tStartRefresh)
    trials.addData('skey_resp.stopped', skey_resp.tStopRefresh)
    #save data
    trials.addData('nPumps', nPumps)
    #trials.addData('size', balloonSize)
    #trials.addData('popped', popped)
    
    
    trials.addData('balloonBody.started', balloonBody.tStartRefresh)
    trials.addData('balloonBody.stopped', balloonBody.tStopRefresh)
    trials.addData('reminderMsg.started', reminderMsg.tStartRefresh)
    trials.addData('reminderMsg.stopped', reminderMsg.tStopRefresh)
    trials.addData('balloonValMsg.started', balloonValMsg.tStartRefresh)
    trials.addData('balloonValMsg.stopped', balloonValMsg.tStopRefresh)
    
    # ------Prepare to start Routine "effort_evaluation"-------
    continueRoutine = True
    # update component parameters for each repeat
    slider.reset()
    ok_confirmation.keys = []
    ok_confirmation.rt = []
    _ok_confirmation_allKeys = []
    # keep track of which components have finished
    effort_evaluationComponents = [instr_evaluation, slider, evaluation_show, ok_confirmation]
    for thisComponent in effort_evaluationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    effort_evaluationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "effort_evaluation"-------
    while continueRoutine:
        # get current time
        t = effort_evaluationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=effort_evaluationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instr_evaluation* updates
        if instr_evaluation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_evaluation.frameNStart = frameN  # exact frame index
            instr_evaluation.tStart = t  # local t and not account for scr refresh
            instr_evaluation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_evaluation, 'tStartRefresh')  # time at next scr refresh
            instr_evaluation.setAutoDraw(True)
        
        # *slider* updates
        if slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider.frameNStart = frameN  # exact frame index
            slider.tStart = t  # local t and not account for scr refresh
            slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
            slider.setAutoDraw(True)
        if not slider.getRating():
            show_num = ''
        else:
            show_num = str(round(slider.getRating()*100, 2)) + '%'
        
        # *evaluation_show* updates
        if evaluation_show.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            evaluation_show.frameNStart = frameN  # exact frame index
            evaluation_show.tStart = t  # local t and not account for scr refresh
            evaluation_show.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(evaluation_show, 'tStartRefresh')  # time at next scr refresh
            evaluation_show.setAutoDraw(True)
        if evaluation_show.status == STARTED:  # only update if drawing
            evaluation_show.setText(show_num, log=False)
        
        # *ok_confirmation* updates
        if ok_confirmation.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ok_confirmation.frameNStart = frameN  # exact frame index
            ok_confirmation.tStart = t  # local t and not account for scr refresh
            ok_confirmation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ok_confirmation, 'tStartRefresh')  # time at next scr refresh
            ok_confirmation.status = STARTED
            # keyboard checking is just starting
            ok_confirmation.clock.reset()  # now t=0
            ok_confirmation.clearEvents(eventType='keyboard')
        if ok_confirmation.status == STARTED:
            theseKeys = ok_confirmation.getKeys(keyList=['q'], waitRelease=False)
            _ok_confirmation_allKeys.extend(theseKeys)
            if len(_ok_confirmation_allKeys):
                ok_confirmation.keys = _ok_confirmation_allKeys[-1].name  # just the last key pressed
                ok_confirmation.rt = _ok_confirmation_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in effort_evaluationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "effort_evaluation"-------
    for thisComponent in effort_evaluationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('instr_evaluation.started', instr_evaluation.tStartRefresh)
    trials.addData('instr_evaluation.stopped', instr_evaluation.tStopRefresh)
    trials.addData('slider.response', slider.getRating())
    trials.addData('slider.rt', slider.getRT())
    trials.addData('slider.started', slider.tStartRefresh)
    trials.addData('slider.stopped', slider.tStopRefresh)
    trials.addData('evaluation_show.started', evaluation_show.tStartRefresh)
    trials.addData('evaluation_show.stopped', evaluation_show.tStopRefresh)
    # check responses
    if ok_confirmation.keys in ['', [], None]:  # No response was made
        ok_confirmation.keys = None
    trials.addData('ok_confirmation.keys',ok_confirmation.keys)
    if ok_confirmation.keys != None:  # we had a response
        trials.addData('ok_confirmation.rt', ok_confirmation.rt)
    trials.addData('ok_confirmation.started', ok_confirmation.tStart)
    trials.addData('ok_confirmation.stopped', ok_confirmation.tStop)
    # the Routine "effort_evaluation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    print('FB start')
    feedbackMsg.setText(feedback)
    # keep track of which components have finished
    feedbackComponents = [feedbackMsg]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if nPumps > 10:
            if random()<0.8:
                feedback = '恭喜!您成功帮助了对方玩家'
                thisExp.addData('feedbackType', 'good')
            else:
                feedback = '对不起，您未帮助到对方玩家'
                thisExp.addData('feedbackType', 'bad')
        else:
            feedback = '对不起，您未帮助到对方玩家'
            thisExp.addData('feedbackType', 'bad')
        
        
        # *feedbackMsg* updates
        if feedbackMsg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedbackMsg.frameNStart = frameN  # exact frame index
            feedbackMsg.tStart = t  # local t and not account for scr refresh
            feedbackMsg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedbackMsg, 'tStartRefresh')  # time at next scr refresh
            feedbackMsg.setAutoDraw(True)
        if feedbackMsg.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedbackMsg.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                feedbackMsg.tStop = t  # not accounting for scr refresh
                feedbackMsg.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedbackMsg, 'tStopRefresh')  # time at next scr refresh
                feedbackMsg.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('feedbackMsg.started', feedbackMsg.tStartRefresh)
    trials.addData('feedbackMsg.stopped', feedbackMsg.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# ------Prepare to start Routine "final"-------
continueRoutine = True
# update component parameters for each repeat
doneKey.keys = []
doneKey.rt = []
_doneKey_allKeys = []
# keep track of which components have finished
finalComponents = [final_bank, doneKey]
for thisComponent in finalComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
finalClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "final"-------
while continueRoutine:
    # get current time
    t = finalClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=finalClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *final_bank* updates
    if final_bank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        final_bank.frameNStart = frameN  # exact frame index
        final_bank.tStart = t  # local t and not account for scr refresh
        final_bank.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(final_bank, 'tStartRefresh')  # time at next scr refresh
        final_bank.setAutoDraw(True)
    
    # *doneKey* updates
    waitOnFlip = False
    if doneKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        doneKey.frameNStart = frameN  # exact frame index
        doneKey.tStart = t  # local t and not account for scr refresh
        doneKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(doneKey, 'tStartRefresh')  # time at next scr refresh
        doneKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(doneKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(doneKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if doneKey.status == STARTED and not waitOnFlip:
        theseKeys = doneKey.getKeys(keyList=['space'], waitRelease=False)
        _doneKey_allKeys.extend(theseKeys)
        if len(_doneKey_allKeys):
            doneKey.keys = _doneKey_allKeys[-1].name  # just the last key pressed
            doneKey.rt = _doneKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in finalComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "final"-------
for thisComponent in finalComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('final_bank.started', final_bank.tStartRefresh)
thisExp.addData('final_bank.stopped', final_bank.tStopRefresh)
# check responses
if doneKey.keys in ['', [], None]:  # No response was made
    doneKey.keys = None
thisExp.addData('doneKey.keys',doneKey.keys)
if doneKey.keys != None:  # we had a response
    thisExp.addData('doneKey.rt', doneKey.rt)
thisExp.addData('doneKey.started', doneKey.tStartRefresh)
thisExp.addData('doneKey.stopped', doneKey.tStopRefresh)
thisExp.nextEntry()
# the Routine "final" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
