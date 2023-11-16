# NasConfigFault

Base class for all network-attached storage configuration faults.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Nas datastore being configured.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.nas_config_fault import NasConfigFault

# TODO update the JSON string below
json = "{}"
# create an instance of NasConfigFault from a JSON string
nas_config_fault_instance = NasConfigFault.from_json(json)
# print the JSON string representation of the object
print NasConfigFault.to_json()

# convert the object into a dict
nas_config_fault_dict = nas_config_fault_instance.to_dict()
# create an instance of NasConfigFault from a dict
nas_config_fault_form_dict = nas_config_fault.from_dict(nas_config_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


