# HostHardwareElementInfo

Data object describing the operational status of a physical element.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the physical element  ***Since:*** VI API 2.5  | 
**status** | [**ElementDescription**](ElementDescription.md) |  | 

## Example

```python
from vmware_vi.models.host_hardware_element_info import HostHardwareElementInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostHardwareElementInfo from a JSON string
host_hardware_element_info_instance = HostHardwareElementInfo.from_json(json)
# print the JSON string representation of the object
print HostHardwareElementInfo.to_json()

# convert the object into a dict
host_hardware_element_info_dict = host_hardware_element_info_instance.to_dict()
# create an instance of HostHardwareElementInfo from a dict
host_hardware_element_info_form_dict = host_hardware_element_info.from_dict(host_hardware_element_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


