# DesiredSoftwareSpecComponentSpec

Component information for the ESX host.  ***Since:*** vSphere API 7.0.2.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the component.  ***Since:*** vSphere API 7.0.2.0  | 
**version** | **str** | Version of the component.  This field is required in the current release.  ***Since:*** vSphere API 7.0.2.0  | [optional] 

## Example

```python
from vmware_vi.models.desired_software_spec_component_spec import DesiredSoftwareSpecComponentSpec

# TODO update the JSON string below
json = "{}"
# create an instance of DesiredSoftwareSpecComponentSpec from a JSON string
desired_software_spec_component_spec_instance = DesiredSoftwareSpecComponentSpec.from_json(json)
# print the JSON string representation of the object
print DesiredSoftwareSpecComponentSpec.to_json()

# convert the object into a dict
desired_software_spec_component_spec_dict = desired_software_spec_component_spec_instance.to_dict()
# create an instance of DesiredSoftwareSpecComponentSpec from a dict
desired_software_spec_component_spec_form_dict = desired_software_spec_component_spec.from_dict(desired_software_spec_component_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


