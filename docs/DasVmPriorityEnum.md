# DasVmPriorityEnum

Deprecated as of VI API 2.5, use *ClusterDasVmSettingsRestartPriority_enum*.  The priority of the virtual machine determines the preference given to it if sufficient capacity is not available to power on all failed virtual machines.  For example, high priority virtual machines on a host get preference over low priority virtual machines.  Possible values: - `disabled`: vSphere HA is disabled for this virtual machine. - `low`: Virtual machines with this priority have a lower chance of powering on after a   failure if there is insufficient capacity on hosts to meet all virtual machine   needs. - `medium`: Virtual machines with this priority have an intermediate chance of powering   on after a failure if there is insufficient capacity on hosts to meet all   virtual machine needs. - `high`: Virtual machines with this priority have a higher chance of powering on after a   failure if there is insufficient capacity on hosts to meet all virtual machine   needs. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


