# FaultToleranceConfigInfo

FaultToleranceConfigInfo is a data object type containing Fault Tolerance settings for this virtual machine.  role, instanceUuids and configPaths contain information about the whole fault tolerance group.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **int** | The index of the current VM in instanceUuids array starting from 1, so 1 means that it is the primary VM.  ***Since:*** vSphere API 4.0  | 
**instance_uuids** | **List[str]** | The instanceUuid of all the VMs in this fault tolerance group.  The first element is the instanceUuid of the primary VM.  ***Since:*** vSphere API 4.0  | 
**config_paths** | **List[str]** | The configuration file path for all the VMs in this fault tolerance group.  ***Since:*** vSphere API 4.0  | 
**orphaned** | **bool** | Indicates whether a secondary VM is orphaned (no longer associated with the primary VM).  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.fault_tolerance_config_info import FaultToleranceConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FaultToleranceConfigInfo from a JSON string
fault_tolerance_config_info_instance = FaultToleranceConfigInfo.from_json(json)
# print the JSON string representation of the object
print FaultToleranceConfigInfo.to_json()

# convert the object into a dict
fault_tolerance_config_info_dict = fault_tolerance_config_info_instance.to_dict()
# create an instance of FaultToleranceConfigInfo from a dict
fault_tolerance_config_info_form_dict = fault_tolerance_config_info.from_dict(fault_tolerance_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


