# ActionParameterEnum

These constant strings can be used as parameters in user-specified email subject and body templates as well as in scripts.  The action processor in VirtualCenter substitutes the run-time values for the parameters. For example, an email subject provided by the client could be the string: `Alarm - {alarmName} Description:\\n{eventDescription}`. Or a script action provided could be: `myScript {alarmName}`.  Possible values: - `targetName`: The name of the entity where the alarm is triggered. - `alarmName`: The name of the triggering alarm. - `oldStatus`: The status prior to the alarm being triggered. - `newStatus`: The status after the alarm is triggered. - `triggeringSummary`: A summary of information involved in triggering the alarm. - `declaringSummary`: A summary of declarations made during the triggering of the alarm. - `eventDescription`: The event description. - `target`: The object of the entity where the alarm is associated. - `alarm`: The object of the triggering alarm. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


