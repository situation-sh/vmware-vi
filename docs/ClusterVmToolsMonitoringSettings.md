# ClusterVmToolsMonitoringSettings

The *ClusterVmToolsMonitoringSettings* data object contains virtual machine monitoring settings that are used by the Virtual Machine Health Monitoring Service.  The Service checks the VMware Tools heartbeat of a virtual machine. If heartbeats have not been received within a specified time interval, the Service declares the virtual machine as failed and resets the virtual machine.  These settings are applied to individual virtual machines during cluster reconfiguration (*ClusterDasVmConfigInfo*.*ClusterDasVmConfigInfo.dasSettings*.*ClusterDasVmSettings.vmToolsMonitoringSettings*). You can also specify them as default values (*ClusterDasConfigInfo*.*ClusterDasConfigInfo.defaultVmSettings*).  All fields are optional. In case of a reconfiguration, fields left unset are not changed.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Deprecated as of vSphere API 4.1, use *ClusterVmToolsMonitoringSettings.vmMonitoring*.  Flag indicating whether or not the Virtual Machine Health Monitoring service is enabled.  The Server does not use this property.  ***Since:*** vSphere API 4.0  | [optional] 
**vm_monitoring** | **str** | Indicates the type of virtual machine monitoring.  Specify a string value corresponding to one of the following *ClusterDasConfigInfoVmMonitoringState_enum* values: - &lt;code&gt;vmMonitoringDisabled&lt;/code&gt; (the default value) - &lt;code&gt;vmMonitoringOnly&lt;/code&gt; - &lt;code&gt;vmAndAppMonitoring&lt;/code&gt;    The individual VMware Tools setting for virtual machine monitoring depends on the HA Virtual Machine Health Monitoring Service level that is defined for the cluster (*ClusterDasConfigInfo*.*ClusterDasConfigInfo.vmMonitoring*). The following list indicates the supported VMware Tools &lt;code&gt;vmMonitoring&lt;/code&gt; values according to the cluster configuration. - If the cluster configuration specifies &lt;code&gt;vmMonitoringDisabled&lt;/code&gt;,   the Service is disabled and the HA Service ignores the VMware Tools monitoring setting. - If the cluster configuration specifies &lt;code&gt;vmMonitoringOnly&lt;/code&gt;,   the Service supports &lt;code&gt;vmMonitoringOnly&lt;/code&gt; or &lt;code&gt;vmMonitoringDisabled&lt;/code&gt; only. - If the cluster configuration specifies &lt;code&gt;vmAndAppMonitoring&lt;/code&gt;,   you can use any of the *ClusterDasConfigInfoVmMonitoringState_enum* values.    The *ClusterVmToolsMonitoringSettings.clusterSettings* value has no effect on the constraint imposed by the HA Virtual Machine Health Monitoring Service level that is defined for the cluster (*ClusterDasConfigInfo*.*ClusterDasConfigInfo.vmMonitoring*).  Application monitoring events are generated regardless of the currently configured type of virtual machine monitoring. You can use these events even if monitoring is being disabled or set to &lt;code&gt;vmMonitoringOnly&lt;/code&gt;.  ***Since:*** vSphere API 4.1  | [optional] 
**cluster_settings** | **bool** | Flag indicating whether to use the cluster settings or the per VM settings.  The default value is true.  ***Since:*** vSphere API 4.0  | [optional] 
**failure_interval** | **int** | If no heartbeat has been received for at least the specified number of seconds, the virtual machine is declared as failed.  The default value is 30.  ***Since:*** vSphere API 4.0  | [optional] 
**min_up_time** | **int** | The number of seconds for the virtual machine&#39;s heartbeats to stabilize after the virtual machine has been powered on.  This time should include the guest operating system boot-up time. The virtual machine monitoring will begin only after this period.  The default value is 120.  ***Since:*** vSphere API 4.0  | [optional] 
**max_failures** | **int** | Maximum number of failures and automated resets allowed during the time that *ClusterVmToolsMonitoringSettings.maxFailureWindow* specifies.  If *ClusterVmToolsMonitoringSettings.maxFailureWindow* is -1 (no window), this represents the absolute number of failures after which automated response is stopped.  If a virtual machine exceeds this threshold, in-depth problem analysis is usually needed.  The default value is 3.  ***Since:*** vSphere API 4.0  | [optional] 
**max_failure_window** | **int** | The number of seconds for the window during which up to *ClusterVmToolsMonitoringSettings.maxFailures* resets can occur before automated responses stop.  If set to -1, no failure window is specified.  The default value is -1.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.cluster_vm_tools_monitoring_settings import ClusterVmToolsMonitoringSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterVmToolsMonitoringSettings from a JSON string
cluster_vm_tools_monitoring_settings_instance = ClusterVmToolsMonitoringSettings.from_json(json)
# print the JSON string representation of the object
print ClusterVmToolsMonitoringSettings.to_json()

# convert the object into a dict
cluster_vm_tools_monitoring_settings_dict = cluster_vm_tools_monitoring_settings_instance.to_dict()
# create an instance of ClusterVmToolsMonitoringSettings from a dict
cluster_vm_tools_monitoring_settings_form_dict = cluster_vm_tools_monitoring_settings.from_dict(cluster_vm_tools_monitoring_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


