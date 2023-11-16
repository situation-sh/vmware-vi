# FaultToleranceSecondaryConfigInfo

FaultToleranceSecondaryConfigInfo is a data object type containing Fault Tolerance settings for a secondary virtual machine in a fault tolerance group  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.fault_tolerance_secondary_config_info import FaultToleranceSecondaryConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FaultToleranceSecondaryConfigInfo from a JSON string
fault_tolerance_secondary_config_info_instance = FaultToleranceSecondaryConfigInfo.from_json(json)
# print the JSON string representation of the object
print FaultToleranceSecondaryConfigInfo.to_json()

# convert the object into a dict
fault_tolerance_secondary_config_info_dict = fault_tolerance_secondary_config_info_instance.to_dict()
# create an instance of FaultToleranceSecondaryConfigInfo from a dict
fault_tolerance_secondary_config_info_form_dict = fault_tolerance_secondary_config_info.from_dict(fault_tolerance_secondary_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


