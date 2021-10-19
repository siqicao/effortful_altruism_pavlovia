/*********************** 
 * Effortful_Help Test *
 ***********************/

import { PsychoJS } from './lib/core-2020.2.js';
import * as core from './lib/core-2020.2.js';
import { TrialHandler } from './lib/data-2020.2.js';
import { Scheduler } from './lib/util-2020.2.js';
import * as visual from './lib/visual-2020.2.js';
import * as sound from './lib/sound-2020.2.js';
import * as util from './lib/util-2020.2.js';
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'norm',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'effortful_help';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'gender': ['1: male', '0: female'], 'age': '', 'session': '001', 'Alipay(支付宝账户)': ''};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(instructionsRoutineBegin());
flowScheduler.add(instructionsRoutineEachFrame());
flowScheduler.add(instructionsRoutineEnd());
flowScheduler.add(roleAssignRoutineBegin());
flowScheduler.add(roleAssignRoutineEachFrame());
flowScheduler.add(roleAssignRoutineEnd());
flowScheduler.add(rewardExplainRoutineBegin());
flowScheduler.add(rewardExplainRoutineEachFrame());
flowScheduler.add(rewardExplainRoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin, trialsLoopScheduler);
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(finalRoutineBegin());
flowScheduler.add(finalRoutineEachFrame());
flowScheduler.add(finalRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  });

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.DEBUG);


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2020.2.4';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var instructionsClock;
var random;
var event;
var round;
var thisExp;
var instrMessage;
var resp;
var name_list;
var nameShow;
var roleAssignClock;
var instr_role;
var key_resp_1;
var role_assign;
var rewardExplainClock;
var instr_reward;
var key_resp_2;
var reward_explain;
var fixationClock;
var tiral_cue;
var waitingClock;
var waitText;
var countdown_2s;
var countdown_1s;
var waitForOutcome;
var loss_levelClock;
var name;
var loss_level1;
var loss_level2;
var loss_level3;
var EffortTaskClock;
var skey_resp;
var balloonSize;
var balloonMsgHeight;
var balloonBody;
var reminderMsg;
var balloonValMsg;
var effort_evaluationClock;
var instr_evaluation;
var effort;
var effort_evaluation_show;
var ok_1;
var feedbackClock;
var feedback;
var feedbackMsg;
var finalClock;
var final_bank;
var doneKey;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "instructions"
  instructionsClock = new util.Clock();
  random = Math.random;
  event = psychoJS.eventManager;
  round = function(num, n=0){
      return +(Math.round(num+('e+'+n)) + ('e-'+n));
  }
  thisExp = psychoJS.experiment;
  instrMessage = new visual.TextStim({
    win: psychoJS.window,
    name: 'instrMessage',
    text: '您好，欢迎参加实验！ 实验共有两轮，你会与1名其他参与者共同完成实验。 每轮实验您将会被分配到一种角色：1）助人者；2）求助者。  请按空格键[space]继续',
    font: 'simkai',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color([1.0, 1.0, 1.0]),  opacity: 1,
    depth: -1.0 
  });
  
  resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  name_list = ["liqiyu", "xiaomingcheng", "quanyuwen"];
  nameShow = name_list[Number.parseInt((random() * name_list.length))];
  
  // Initialize components for Routine "roleAssign"
  roleAssignClock = new util.Clock();
  instr_role = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_role',
    text: '理解后，请按空格键[space]继续 ',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.6)], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color([1.0, 1.0, 1.0]),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  role_assign = new visual.ImageStim({
    win : psychoJS.window,
    name : 'role_assign', units : undefined, 
    image : 'instru_role.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [1, 1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -2.0 
  });
  // Initialize components for Routine "rewardExplain"
  rewardExplainClock = new util.Clock();
  instr_reward = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_reward',
    text: '您可以根据自己的意愿帮助他人减少损失 理解后，请按空格键[space]继续 ',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.6)], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color([1.0, 1.0, 1.0]),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  reward_explain = new visual.ImageStim({
    win : psychoJS.window,
    name : 'reward_explain', units : undefined, 
    image : 'reward_explain.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [1, 1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -2.0 
  });
  // Initialize components for Routine "fixation"
  fixationClock = new util.Clock();
  tiral_cue = new visual.ImageStim({
    win : psychoJS.window,
    name : 'tiral_cue', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.5, 0.6],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -1.0 
  });
  // Initialize components for Routine "waiting"
  waitingClock = new util.Clock();
  waitText = new visual.TextStim({
    win: psychoJS.window,
    name: 'waitText',
    text: '请您耐心等待另外一名玩家2s小游戏 您将会看到根据ta的任务表现计算的损失水平',
    font: 'simsun',
    units: undefined, 
    pos: [0, 0], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color([1.0, 1.0, 1.0]),  opacity: 1,
    depth: 0.0 
  });
  
  countdown_2s = new visual.TextStim({
    win: psychoJS.window,
    name: 'countdown_2s',
    text: '请等待 2s',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color([1.0, 1.0, 1.0]),  opacity: 1,
    depth: -1.0 
  });
  
  countdown_1s = new visual.TextStim({
    win: psychoJS.window,
    name: 'countdown_1s',
    text: '请等待 1s',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color([1.0, 1.0, 1.0]),  opacity: 1,
    depth: -2.0 
  });
  
  waitForOutcome = new visual.TextStim({
    win: psychoJS.window,
    name: 'waitForOutcome',
    text: '请等待结果计算…',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "loss_level"
  loss_levelClock = new util.Clock();
  name = new visual.TextStim({
    win: psychoJS.window,
    name: 'name',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.6], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color([1.0, 1.0, 1.0]),  opacity: 1,
    depth: -1.0 
  });
  
  loss_level1 = new visual.Rect ({
    win: psychoJS.window, name: 'loss_level1', 
    width: [0.2, 0.2][0], height: [0.2, 0.2][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 0.5, depth: -2, interpolate: true,
  });
  
  loss_level2 = new visual.Rect ({
    win: psychoJS.window, name: 'loss_level2', 
    width: [0.2, 0.2][0], height: [0.2, 0.2][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 0.765), 0.129, 1.0]),
    opacity: 0.5, depth: -3, interpolate: true,
  });
  
  loss_level3 = new visual.Rect ({
    win: psychoJS.window, name: 'loss_level3', 
    width: [0.2, 0.2][0], height: [0.2, 0.2][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([0.867, (- 0.655), (- 0.655)]),
    opacity: 0.5, depth: -4, interpolate: true,
  });
  
  // Initialize components for Routine "EffortTask"
  EffortTaskClock = new util.Clock();
  skey_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  balloonSize = 0.08;
  balloonMsgHeight = 0.01;
  
  balloonBody = new visual.ImageStim({
    win : psychoJS.window,
    name : 'balloonBody', units : undefined, 
    image : 'redBalloon.png', mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  reminderMsg = new visual.TextStim({
    win: psychoJS.window,
    name: 'reminderMsg',
    text: '请按空格键 [space]将气球充气',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.8)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color([1.0, 1.0, 1.0]),  opacity: 1,
    depth: -3.0 
  });
  
  balloonValMsg = new visual.TextStim({
    win: psychoJS.window,
    name: 'balloonValMsg',
    text: '为了帮助他人减少损失： 请您在3s内尽可能的将气球充气打！ 任务失败则没有办法帮助他人',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.05], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color([1.0, 1.0, 1.0]),  opacity: 1,
    depth: -4.0 
  });
  
  // Initialize components for Routine "effort_evaluation"
  effort_evaluationClock = new util.Clock();
  instr_evaluation = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_evaluation',
    text: "请您评价自己在气球任务中的努力程度 请点击‘Q'键表示“确定”",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color([1.0, 1.0, 1.0]),  opacity: 1,
    depth: 0.0 
  });
  
  effort = new visual.Slider({
    win: psychoJS.window, name: 'effort',
    size: [1.0, 0.1], pos: [0, (- 0.3)], units: 'norm',
    labels: ["0%", "100%"], ticks: [0, 1],
    granularity: 0, style: [visual.Slider.Style.RATING],
    color: new util.Color('LightGray'), 
    fontFamily: 'HelveticaBold', bold: true, italic: false, 
    flip: false,
  });
  
  effort_evaluation_show = new visual.TextStim({
    win: psychoJS.window,
    name: 'effort_evaluation_show',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color([1.0, 1.0, 1.0]),  opacity: 1,
    depth: -3.0 
  });
  
  ok_1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "feedback"
  feedbackClock = new util.Clock();
  feedback = "\u606d\u559c!\u60a8\u6210\u529f\u5e2e\u52a9\u4e86\u5bf9\u65b9\u73a9\u5bb6";
  
  feedbackMsg = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedbackMsg',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color([1.0, 1.0, 1.0]),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "final"
  finalClock = new util.Clock();
  final_bank = new visual.TextStim({
    win: psychoJS.window,
    name: 'final_bank',
    text: '您的账户已存入18元 在您实验后1-2天内，主试会将您的被试费打入您的账户。\n结束时，请勿立即退出。\n数据传输需要2-3min，请务必向主试确认是否成功收到数据！\n请按空格键[space]退出',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color([1.0, 1.0, 1.0]),  opacity: 1,
    depth: 0.0 
  });
  
  doneKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var _resp_allKeys;
var instructionsComponents;
function instructionsRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'instructions'-------
    t = 0;
    instructionsClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    resp.keys = undefined;
    resp.rt = undefined;
    _resp_allKeys = [];
    // keep track of which components have finished
    instructionsComponents = [];
    instructionsComponents.push(instrMessage);
    instructionsComponents.push(resp);
    
    for (const thisComponent of instructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


var continueRoutine;
function instructionsRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'instructions'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instrMessage* updates
    if (t >= 0.0 && instrMessage.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instrMessage.tStart = t;  // (not accounting for frame time here)
      instrMessage.frameNStart = frameN;  // exact frame index
      
      instrMessage.setAutoDraw(true);
    }

    
    // *resp* updates
    if (t >= 0.0 && resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resp.tStart = t;  // (not accounting for frame time here)
      resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { resp.clearEvents(); });
    }

    if (resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = resp.getKeys({keyList: ['space'], waitRelease: false});
      _resp_allKeys = _resp_allKeys.concat(theseKeys);
      if (_resp_allKeys.length > 0) {
        resp.keys = _resp_allKeys[_resp_allKeys.length - 1].name;  // just the last key pressed
        resp.rt = _resp_allKeys[_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instructionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructionsRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'instructions'-------
    for (const thisComponent of instructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('resp.keys', resp.keys);
    if (typeof resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('resp.rt', resp.rt);
        routineTimer.reset();
        }
    
    resp.stop();
    // the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_1_allKeys;
var roleAssignComponents;
function roleAssignRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'roleAssign'-------
    t = 0;
    roleAssignClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_1.keys = undefined;
    key_resp_1.rt = undefined;
    _key_resp_1_allKeys = [];
    // keep track of which components have finished
    roleAssignComponents = [];
    roleAssignComponents.push(instr_role);
    roleAssignComponents.push(key_resp_1);
    roleAssignComponents.push(role_assign);
    
    for (const thisComponent of roleAssignComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function roleAssignRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'roleAssign'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = roleAssignClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instr_role* updates
    if (t >= 0.0 && instr_role.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr_role.tStart = t;  // (not accounting for frame time here)
      instr_role.frameNStart = frameN;  // exact frame index
      
      instr_role.setAutoDraw(true);
    }

    
    // *key_resp_1* updates
    if (t >= 0.0 && key_resp_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_1.tStart = t;  // (not accounting for frame time here)
      key_resp_1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_1.clearEvents(); });
    }

    if (key_resp_1.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_1.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_1_allKeys = _key_resp_1_allKeys.concat(theseKeys);
      if (_key_resp_1_allKeys.length > 0) {
        key_resp_1.keys = _key_resp_1_allKeys[_key_resp_1_allKeys.length - 1].name;  // just the last key pressed
        key_resp_1.rt = _key_resp_1_allKeys[_key_resp_1_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *role_assign* updates
    if (t >= 0.0 && role_assign.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      role_assign.tStart = t;  // (not accounting for frame time here)
      role_assign.frameNStart = frameN;  // exact frame index
      
      role_assign.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of roleAssignComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function roleAssignRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'roleAssign'-------
    for (const thisComponent of roleAssignComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key_resp_1.keys', key_resp_1.keys);
    if (typeof key_resp_1.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_1.rt', key_resp_1.rt);
        routineTimer.reset();
        }
    
    key_resp_1.stop();
    // the Routine "roleAssign" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_2_allKeys;
var rewardExplainComponents;
function rewardExplainRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'rewardExplain'-------
    t = 0;
    rewardExplainClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // keep track of which components have finished
    rewardExplainComponents = [];
    rewardExplainComponents.push(instr_reward);
    rewardExplainComponents.push(key_resp_2);
    rewardExplainComponents.push(reward_explain);
    
    for (const thisComponent of rewardExplainComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function rewardExplainRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'rewardExplain'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = rewardExplainClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instr_reward* updates
    if (t >= 0.0 && instr_reward.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr_reward.tStart = t;  // (not accounting for frame time here)
      instr_reward.frameNStart = frameN;  // exact frame index
      
      instr_reward.setAutoDraw(true);
    }

    
    // *key_resp_2* updates
    if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }

    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *reward_explain* updates
    if (t >= 0.0 && reward_explain.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      reward_explain.tStart = t;  // (not accounting for frame time here)
      reward_explain.frameNStart = frameN;  // exact frame index
      
      reward_explain.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of rewardExplainComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function rewardExplainRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'rewardExplain'-------
    for (const thisComponent of rewardExplainComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        routineTimer.reset();
        }
    
    key_resp_2.stop();
    // the Routine "rewardExplain" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var trials;
var currentLoop;
function trialsLoopBegin(trialsLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'trialTypes_effort.xlsx',
    seed: undefined, name: 'trials'
  });
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment
  currentLoop = trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrial of trials) {
    const snapshot = trials.getSnapshot();
    trialsLoopScheduler.add(importConditions(snapshot));
    trialsLoopScheduler.add(fixationRoutineBegin(snapshot));
    trialsLoopScheduler.add(fixationRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(fixationRoutineEnd(snapshot));
    trialsLoopScheduler.add(waitingRoutineBegin(snapshot));
    trialsLoopScheduler.add(waitingRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(waitingRoutineEnd(snapshot));
    trialsLoopScheduler.add(loss_levelRoutineBegin(snapshot));
    trialsLoopScheduler.add(loss_levelRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(loss_levelRoutineEnd(snapshot));
    trialsLoopScheduler.add(EffortTaskRoutineBegin(snapshot));
    trialsLoopScheduler.add(EffortTaskRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(EffortTaskRoutineEnd(snapshot));
    trialsLoopScheduler.add(effort_evaluationRoutineBegin(snapshot));
    trialsLoopScheduler.add(effort_evaluationRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(effort_evaluationRoutineEnd(snapshot));
    trialsLoopScheduler.add(feedbackRoutineBegin(snapshot));
    trialsLoopScheduler.add(feedbackRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(feedbackRoutineEnd(snapshot));
    trialsLoopScheduler.add(endLoopIteration(trialsLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}


var fixationPic;
var fixationComponents;
function fixationRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'fixation'-------
    t = 0;
    fixationClock.reset(); // clock
    frameN = -1;
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    if ((pay_type < 1)) {
        fixationPic = "nonself_pay.png";
    } else {
        fixationPic = "self_pay.png";
    }
    
    tiral_cue.setImage(fixationPic);
    // keep track of which components have finished
    fixationComponents = [];
    fixationComponents.push(tiral_cue);
    
    for (const thisComponent of fixationComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


var frameRemains;
function fixationRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'fixation'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = fixationClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *tiral_cue* updates
    if (t >= 0.0 && tiral_cue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      tiral_cue.tStart = t;  // (not accounting for frame time here)
      tiral_cue.frameNStart = frameN;  // exact frame index
      
      tiral_cue.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (tiral_cue.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      tiral_cue.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of fixationComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fixationRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'fixation'-------
    for (const thisComponent of fixationComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var waitingComponents;
function waitingRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'waiting'-------
    t = 0;
    waitingClock.reset(); // clock
    frameN = -1;
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    waitingComponents = [];
    waitingComponents.push(waitText);
    waitingComponents.push(countdown_2s);
    waitingComponents.push(countdown_1s);
    waitingComponents.push(waitForOutcome);
    
    for (const thisComponent of waitingComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function waitingRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'waiting'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = waitingClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *waitText* updates
    if (t >= 0.0 && waitText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      waitText.tStart = t;  // (not accounting for frame time here)
      waitText.frameNStart = frameN;  // exact frame index
      
      waitText.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (waitText.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      waitText.setAutoDraw(false);
    }
    
    // *countdown_2s* updates
    if (t >= 0.0 && countdown_2s.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      countdown_2s.tStart = t;  // (not accounting for frame time here)
      countdown_2s.frameNStart = frameN;  // exact frame index
      
      countdown_2s.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (countdown_2s.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      countdown_2s.setAutoDraw(false);
    }
    
    // *countdown_1s* updates
    if (t >= 1.0 && countdown_1s.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      countdown_1s.tStart = t;  // (not accounting for frame time here)
      countdown_1s.frameNStart = frameN;  // exact frame index
      
      countdown_1s.setAutoDraw(true);
    }

    frameRemains = 1.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (countdown_1s.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      countdown_1s.setAutoDraw(false);
    }
    
    // *waitForOutcome* updates
    if (t >= 2.0 && waitForOutcome.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      waitForOutcome.tStart = t;  // (not accounting for frame time here)
      waitForOutcome.frameNStart = frameN;  // exact frame index
      
      waitForOutcome.setAutoDraw(true);
    }

    frameRemains = 2.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (waitForOutcome.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      waitForOutcome.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of waitingComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function waitingRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'waiting'-------
    for (const thisComponent of waitingComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var nameShow_loss;
var pos1;
var pos2;
var pos3;
var loss_levelComponents;
function loss_levelRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'loss_level'-------
    t = 0;
    loss_levelClock.reset(); // clock
    frameN = -1;
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    nameShow_loss = (nameShow + "\u7684\u635f\u5931\u6c34\u5e73\u4e3a");
    pos1 = 0;
    pos2 = 0;
    pos3 = 0;
    if ((opac_1 < 0.1)) {
        pos1 = [5, 5];
    } else {
        pos1 = [0, (- 0.2)];
    }
    if ((opac_2 < 0.1)) {
        pos2 = [5, 5];
    } else {
        pos2 = [0, 0];
    }
    if ((opac_3 < 0.1)) {
        pos3 = [5, 5];
    } else {
        pos3 = [0, 0.2];
    }
    console.log(pos1, pos2, pos3);
    
    name.setText(nameShow_loss);
    loss_level1.setPos([pos1[0], pos1[1]]);
    loss_level2.setPos([pos2[0], pos2[1]]);
    loss_level3.setPos([pos3[0], pos3[1]]);
    // keep track of which components have finished
    loss_levelComponents = [];
    loss_levelComponents.push(name);
    loss_levelComponents.push(loss_level1);
    loss_levelComponents.push(loss_level2);
    loss_levelComponents.push(loss_level3);
    
    for (const thisComponent of loss_levelComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function loss_levelRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'loss_level'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = loss_levelClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *name* updates
    if (t >= 0.0 && name.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      name.tStart = t;  // (not accounting for frame time here)
      name.frameNStart = frameN;  // exact frame index
      
      name.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (name.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      name.setAutoDraw(false);
    }
    
    // *loss_level1* updates
    if (t >= 0.0 && loss_level1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      loss_level1.tStart = t;  // (not accounting for frame time here)
      loss_level1.frameNStart = frameN;  // exact frame index
      
      loss_level1.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (loss_level1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      loss_level1.setAutoDraw(false);
    }
    
    // *loss_level2* updates
    if (t >= 0.0 && loss_level2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      loss_level2.tStart = t;  // (not accounting for frame time here)
      loss_level2.frameNStart = frameN;  // exact frame index
      
      loss_level2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (loss_level2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      loss_level2.setAutoDraw(false);
    }
    
    // *loss_level3* updates
    if (t >= 0.0 && loss_level3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      loss_level3.tStart = t;  // (not accounting for frame time here)
      loss_level3.frameNStart = frameN;  // exact frame index
      
      loss_level3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (loss_level3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      loss_level3.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of loss_levelComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function loss_levelRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'loss_level'-------
    for (const thisComponent of loss_levelComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var _skey_resp_allKeys;
var popped;
var nPumps;
var EffortTaskComponents;
function EffortTaskRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'EffortTask'-------
    t = 0;
    EffortTaskClock.reset(); // clock
    frameN = -1;
    routineTimer.add(4.000000);
    // update component parameters for each repeat
    skey_resp.keys = undefined;
    skey_resp.rt = undefined;
    _skey_resp_allKeys = [];
    balloonSize = 0.08;
    popped = false;
    nPumps = 0;
    
    console.log("start");
    
    // keep track of which components have finished
    EffortTaskComponents = [];
    EffortTaskComponents.push(skey_resp);
    EffortTaskComponents.push(balloonBody);
    EffortTaskComponents.push(reminderMsg);
    EffortTaskComponents.push(balloonValMsg);
    
    for (const thisComponent of EffortTaskComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function EffortTaskRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'EffortTask'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = EffortTaskClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *skey_resp* updates
    if (t >= 1 && skey_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      skey_resp.tStart = t;  // (not accounting for frame time here)
      skey_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { skey_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { skey_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { skey_resp.clearEvents(); });
    }

    frameRemains = 1 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (skey_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      skey_resp.status = PsychoJS.Status.FINISHED;
  }

    if (skey_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = skey_resp.getKeys({keyList: ['space'], waitRelease: false});
      _skey_resp_allKeys = _skey_resp_allKeys.concat(theseKeys);
      if (_skey_resp_allKeys.length > 0) {
        skey_resp.keys = _skey_resp_allKeys.map((key) => key.name);  // storing all keys
        skey_resp.rt = _skey_resp_allKeys.map((key) => key.rt);
      }
    }
    
    balloonSize = (0.1 + (nPumps * 0.015));
    
    
    // *balloonBody* updates
    if (t >= 1.0 && balloonBody.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      balloonBody.tStart = t;  // (not accounting for frame time here)
      balloonBody.frameNStart = frameN;  // exact frame index
      
      balloonBody.setAutoDraw(true);
    }

    frameRemains = 1.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (balloonBody.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      balloonBody.setAutoDraw(false);
    }
    
    if (balloonBody.status === PsychoJS.Status.STARTED){ // only update if being drawn
      balloonBody.setPos([((- 1) + (balloonSize / 2)), 0]);
      balloonBody.setSize(balloonSize);
    }
    
    // *reminderMsg* updates
    if (t >= 1.0 && reminderMsg.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      reminderMsg.tStart = t;  // (not accounting for frame time here)
      reminderMsg.frameNStart = frameN;  // exact frame index
      
      reminderMsg.setAutoDraw(true);
    }

    frameRemains = 1.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (reminderMsg.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      reminderMsg.setAutoDraw(false);
    }
    
    // *balloonValMsg* updates
    if (t >= 1.0 && balloonValMsg.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      balloonValMsg.tStart = t;  // (not accounting for frame time here)
      balloonValMsg.frameNStart = frameN;  // exact frame index
      
      balloonValMsg.setAutoDraw(true);
    }

    frameRemains = 1.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (balloonValMsg.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      balloonValMsg.setAutoDraw(false);
    }
    if (skey_resp.keys) {
        nPumps = skey_resp.keys.length;
    }
    console.log(nPumps);
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of EffortTaskComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function EffortTaskRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'EffortTask'-------
    for (const thisComponent of EffortTaskComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('skey_resp.keys', skey_resp.keys);
    if (typeof skey_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('skey_resp.rt', skey_resp.rt);
        }
    
    skey_resp.stop();
    trials.addData("nPumps", nPumps);
    
    return Scheduler.Event.NEXT;
  };
}


var _ok_1_allKeys;
var effort_evaluationComponents;
function effort_evaluationRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'effort_evaluation'-------
    t = 0;
    effort_evaluationClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    effort.reset()
    ok_1.keys = undefined;
    ok_1.rt = undefined;
    _ok_1_allKeys = [];
    // keep track of which components have finished
    effort_evaluationComponents = [];
    effort_evaluationComponents.push(instr_evaluation);
    effort_evaluationComponents.push(effort);
    effort_evaluationComponents.push(effort_evaluation_show);
    effort_evaluationComponents.push(ok_1);
    
    for (const thisComponent of effort_evaluationComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


var show_num;
function effort_evaluationRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'effort_evaluation'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = effort_evaluationClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instr_evaluation* updates
    if (t >= 0.0 && instr_evaluation.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr_evaluation.tStart = t;  // (not accounting for frame time here)
      instr_evaluation.frameNStart = frameN;  // exact frame index
      
      instr_evaluation.setAutoDraw(true);
    }

    
    // *effort* updates
    if (t >= 0.0 && effort.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      effort.tStart = t;  // (not accounting for frame time here)
      effort.frameNStart = frameN;  // exact frame index
      
      effort.setAutoDraw(true);
    }

    if ((! effort.getRating())) {
        show_num = "";
    } else {
        show_num = (round((effort.getRating() * 100), 2).toString() + "%");
    }
    
    
    // *effort_evaluation_show* updates
    if (t >= 0.0 && effort_evaluation_show.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      effort_evaluation_show.tStart = t;  // (not accounting for frame time here)
      effort_evaluation_show.frameNStart = frameN;  // exact frame index
      
      effort_evaluation_show.setAutoDraw(true);
    }

    
    if (effort_evaluation_show.status === PsychoJS.Status.STARTED){ // only update if being drawn
      effort_evaluation_show.setText(show_num);
    }
    
    // *ok_1* updates
    if (t >= 0.0 && ok_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ok_1.tStart = t;  // (not accounting for frame time here)
      ok_1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      ok_1.clock.reset();
      ok_1.start();
      ok_1.clearEvents();
    }

    if (ok_1.status === PsychoJS.Status.STARTED) {
      let theseKeys = ok_1.getKeys({keyList: ['q'], waitRelease: false});
      _ok_1_allKeys = _ok_1_allKeys.concat(theseKeys);
      if (_ok_1_allKeys.length > 0) {
        ok_1.keys = _ok_1_allKeys[_ok_1_allKeys.length - 1].name;  // just the last key pressed
        ok_1.rt = _ok_1_allKeys[_ok_1_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of effort_evaluationComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var effort_eva;
function effort_evaluationRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'effort_evaluation'-------
    for (const thisComponent of effort_evaluationComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('effort.response', effort.getRating());
    psychoJS.experiment.addData('effort.rt', effort.getRT());
    effort_eva = slider.getRating();
    thisExp.addData("effort_eva", effort_eva);
    
    psychoJS.experiment.addData('ok_1.keys', ok_1.keys);
    if (typeof ok_1.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('ok_1.rt', ok_1.rt);
        routineTimer.reset();
        }
    
    ok_1.stop();
    // the Routine "effort_evaluation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var feedbackComponents;
function feedbackRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'feedback'-------
    t = 0;
    feedbackClock.reset(); // clock
    frameN = -1;
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    console.log("FB start");
    
    feedbackMsg.setText(feedback);
    // keep track of which components have finished
    feedbackComponents = [];
    feedbackComponents.push(feedbackMsg);
    
    for (const thisComponent of feedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function feedbackRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'feedback'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    if ((nPumps > 10)) {
        if ((random() < 0.8)) {
            feedback = "\u606d\u559c!\u60a8\u6210\u529f\u5e2e\u52a9\u4e86\u5bf9\u65b9\u73a9\u5bb6";
            thisExp.addData("feedbackType", "good");
        } else {
            feedback = "\u5bf9\u4e0d\u8d77\uff0c\u60a8\u672a\u5e2e\u52a9\u5230\u5bf9\u65b9\u73a9\u5bb6";
            thisExp.addData("feedbackType", "bad");
        }
    } else {
        feedback = "\u5bf9\u4e0d\u8d77\uff0c\u60a8\u672a\u5e2e\u52a9\u5230\u5bf9\u65b9\u73a9\u5bb6";
        thisExp.addData("feedbackType", "bad");
    }
    
    
    // *feedbackMsg* updates
    if (t >= 0.0 && feedbackMsg.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedbackMsg.tStart = t;  // (not accounting for frame time here)
      feedbackMsg.frameNStart = frameN;  // exact frame index
      
      feedbackMsg.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (feedbackMsg.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedbackMsg.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function feedbackRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'feedback'-------
    for (const thisComponent of feedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var _doneKey_allKeys;
var finalComponents;
function finalRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'final'-------
    t = 0;
    finalClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    doneKey.keys = undefined;
    doneKey.rt = undefined;
    _doneKey_allKeys = [];
    // keep track of which components have finished
    finalComponents = [];
    finalComponents.push(final_bank);
    finalComponents.push(doneKey);
    
    for (const thisComponent of finalComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function finalRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'final'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = finalClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *final_bank* updates
    if (t >= 0.0 && final_bank.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      final_bank.tStart = t;  // (not accounting for frame time here)
      final_bank.frameNStart = frameN;  // exact frame index
      
      final_bank.setAutoDraw(true);
    }

    
    // *doneKey* updates
    if (t >= 0.0 && doneKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      doneKey.tStart = t;  // (not accounting for frame time here)
      doneKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { doneKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { doneKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { doneKey.clearEvents(); });
    }

    if (doneKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = doneKey.getKeys({keyList: ['space'], waitRelease: false});
      _doneKey_allKeys = _doneKey_allKeys.concat(theseKeys);
      if (_doneKey_allKeys.length > 0) {
        doneKey.keys = _doneKey_allKeys[_doneKey_allKeys.length - 1].name;  // just the last key pressed
        doneKey.rt = _doneKey_allKeys[_doneKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of finalComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function finalRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'final'-------
    for (const thisComponent of finalComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('doneKey.keys', doneKey.keys);
    if (typeof doneKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('doneKey.rt', doneKey.rt);
        routineTimer.reset();
        }
    
    doneKey.stop();
    // the Routine "final" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
