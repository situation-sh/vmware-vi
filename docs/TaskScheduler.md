# TaskScheduler

The *TaskScheduler* data object is the base type for the scheduler objects.  The hierarchy of scheduler objects is as follows:          TaskScheduler             *AfterStartupTaskScheduler*             *OnceTaskScheduler*             *RecurrentTaskScheduler*                 *HourlyTaskScheduler*                     *DailyTaskScheduler*                         *WeeklyTaskScheduler*                         *MonthlyTaskScheduler*                             *MonthlyByDayTaskScheduler*                             *MonthlyByWeekdayTaskScheduler*  Use a scheduler object to set the time(s) for task execution. You can use two scheduling modes - single execution or recurring execution: - Use the *AfterStartupTaskScheduler* or the *OnceTaskScheduler*   to schedule a single instance of task execution. - Use one of the recurrent task schedulers to schedule   hourly, daily, weekly, or monthly task execution.    After you have established the task timing, use the scheduler object for the *ScheduledTaskSpec* *ScheduledTaskSpec.scheduler* property value. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_time** | **datetime** | The time that the schedule for the task takes effect.  Task activation is distinct from task execution. When you activate a task, its schedule starts, and when the next execution time occurs, the task will run. If you do not set activeTime, the activation time defaults to the time that you create the scheduled task.  | [optional] 
**expire_time** | **datetime** | The time the schedule for the task expires.  If you do not set expireTime, the schedule does not expire.  | [optional] 

## Example

```python
from vmware_vi.models.task_scheduler import TaskScheduler

# TODO update the JSON string below
json = "{}"
# create an instance of TaskScheduler from a JSON string
task_scheduler_instance = TaskScheduler.from_json(json)
# print the JSON string representation of the object
print TaskScheduler.to_json()

# convert the object into a dict
task_scheduler_dict = task_scheduler_instance.to_dict()
# create an instance of TaskScheduler from a dict
task_scheduler_form_dict = task_scheduler.from_dict(task_scheduler_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


