# ClusterVmComponentProtectionSettingsStorageVmReactionEnum

The VM policy settings that determine the response to storage failures.  Possible values: - `disabled`: VM Component Protection service will not monitor or react to   the component failure.      This setting does not affect other vSphere   HA services such as Host Monitoring or VM Health Monitoring. - `warning`: VM Component Protection service will monitor component failures but   will not restart an affected VM.      Rather it will notify users about   the component failures. This setting does not affect other vSphere HA   services such as Host Monitoring or VM Health Monitoring. - `restartConservative`: VM Component Protection service protects VMs conservatively.      With this   setting, when the service can't determine that capacity is available to   restart a VM, it will favor keeping the VM running. - `restartAggressive`: VM Component Protection service protects VMs aggressively.      With this setting,   the service will terminate an affected VM even if it can't determine that   capacity exists to restart the VM. - `clusterDefault`: VM will use the cluster default setting.      This option is only meaningful for   per-VM settings.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


