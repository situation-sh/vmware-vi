# OvfNoSpaceOnController

If the hardware element (RASD) point to a parent controller where there is no space left.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent** | **str** | The parent reference  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.ovf_no_space_on_controller import OvfNoSpaceOnController

# TODO update the JSON string below
json = "{}"
# create an instance of OvfNoSpaceOnController from a JSON string
ovf_no_space_on_controller_instance = OvfNoSpaceOnController.from_json(json)
# print the JSON string representation of the object
print OvfNoSpaceOnController.to_json()

# convert the object into a dict
ovf_no_space_on_controller_dict = ovf_no_space_on_controller_instance.to_dict()
# create an instance of OvfNoSpaceOnController from a dict
ovf_no_space_on_controller_form_dict = ovf_no_space_on_controller.from_dict(ovf_no_space_on_controller_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


