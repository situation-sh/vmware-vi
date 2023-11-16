# DasConfigFault

This fault indicates that some error has occurred during the configuration of the host for HA.  This may be subclassed by a more specific fault. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | The reason why the HA configuration failed, if known.  Values should come from *DasConfigFaultDasConfigFaultReason_enum*.  ***Since:*** vSphere API 4.0  | [optional] 
**output** | **str** | The output (stdout/stderr) from executing the configuration.  ***Since:*** vSphere API 4.0  | [optional] 
**event** | [**List[Event]**](Event.md) | The list of events containing details why the configuration failed, if known.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.das_config_fault import DasConfigFault

# TODO update the JSON string below
json = "{}"
# create an instance of DasConfigFault from a JSON string
das_config_fault_instance = DasConfigFault.from_json(json)
# print the JSON string representation of the object
print DasConfigFault.to_json()

# convert the object into a dict
das_config_fault_dict = das_config_fault_instance.to_dict()
# create an instance of DasConfigFault from a dict
das_config_fault_form_dict = das_config_fault.from_dict(das_config_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


