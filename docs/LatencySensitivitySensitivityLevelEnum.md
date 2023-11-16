# LatencySensitivitySensitivityLevelEnum

Enumeration of the nominal latency-sensitive values which can be used to specify the latency-sensitivity level of the application.  In terms of latency-sensitivity the values relate: high&gt;medium&gt;normal&gt;low.  Possible values: - `low`: The relative latency-sensitivity low value. - `normal`: The relative latency-sensitivity normal value.      This is the default latency-sensitivity value. - `medium`: The relative latency-sensitivity medium value. - `high`: The relative latency-sensitivity high value. - `custom`:       Deprecated as of vSphere API Ver 6.0. Value will be ignored and   treated as \"normal\" latency sensitivity.      The custom absolute latency-sensitivity specified in   *LatencySensitivity.sensitivity* property is used to   define the latency-sensitivity.      When this value is set to *LatencySensitivity.level* the   *LatencySensitivity.sensitivity* property should be   set also.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


