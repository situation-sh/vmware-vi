# DesiredSoftwareSpecBaseImageSpec

Describes base-image spec for the ESX host.  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | Version of the base-image.  ***Since:*** vSphere API 7.0  | 

## Example

```python
from vmware_vi.models.desired_software_spec_base_image_spec import DesiredSoftwareSpecBaseImageSpec

# TODO update the JSON string below
json = "{}"
# create an instance of DesiredSoftwareSpecBaseImageSpec from a JSON string
desired_software_spec_base_image_spec_instance = DesiredSoftwareSpecBaseImageSpec.from_json(json)
# print the JSON string representation of the object
print DesiredSoftwareSpecBaseImageSpec.to_json()

# convert the object into a dict
desired_software_spec_base_image_spec_dict = desired_software_spec_base_image_spec_instance.to_dict()
# create an instance of DesiredSoftwareSpecBaseImageSpec from a dict
desired_software_spec_base_image_spec_form_dict = desired_software_spec_base_image_spec.from_dict(desired_software_spec_base_image_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


