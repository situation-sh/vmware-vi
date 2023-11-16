# ClusterVmReadinessReadyConditionEnum

Condition for VM's readiness  Possible values: - `none`: No ready condition specified.      In case of vSphere HA, higher restart priority VMs are still   placed before lower priority VMs. - `poweredOn`: VM is powered on. - `guestHbStatusGreen`: VM guest operating system is up and responding normally (VM tools   heartbeat status is green). - `appHbStatusGreen`: An application running inside the VM is responding normally.      To enable Application Monitoring, you must first obtain the   appropriate SDK (or be using an application that supports VMware   Application Monitoring) and use it to set up customized heartbeats   for the applications you want to monitor.   See *ClusterDasConfigInfo.vmMonitoring*. - `useClusterDefault`: VM will use the cluster default setting.      This option is only   meaningful for per-VM settings.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


