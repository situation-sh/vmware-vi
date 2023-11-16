# InsufficientVFlashResourcesFault

Insufficient vFlash resource to consume  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**free_space_in_mb** | **int** | The vFlash resource available capacity in MB.  ***Since:*** vSphere API 6.0  | [optional] 
**free_space** | **int** | The vFlash resource available capacity in bytes.  ***Since:*** vSphere API 5.5  | 
**requested_space_in_mb** | **int** | The vFlash resource amount requested in MB.  ***Since:*** vSphere API 6.0  | [optional] 
**requested_space** | **int** | The vFlash resource amount requested in bytes.  ***Since:*** vSphere API 5.5  | 

## Example

```python
from vmware_vi.models.insufficient_v_flash_resources_fault import InsufficientVFlashResourcesFault

# TODO update the JSON string below
json = "{}"
# create an instance of InsufficientVFlashResourcesFault from a JSON string
insufficient_v_flash_resources_fault_instance = InsufficientVFlashResourcesFault.from_json(json)
# print the JSON string representation of the object
print InsufficientVFlashResourcesFault.to_json()

# convert the object into a dict
insufficient_v_flash_resources_fault_dict = insufficient_v_flash_resources_fault_instance.to_dict()
# create an instance of InsufficientVFlashResourcesFault from a dict
insufficient_v_flash_resources_fault_form_dict = insufficient_v_flash_resources_fault.from_dict(insufficient_v_flash_resources_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


