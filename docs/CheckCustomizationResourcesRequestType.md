# CheckCustomizationResourcesRequestType

The parameters of *CustomizationSpecManager.CheckCustomizationResources*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guest_os** | **str** | Short name from the guest OS descriptor list describing the OS we intend to customize.  | 

## Example

```python
from vmware_vi.models.check_customization_resources_request_type import CheckCustomizationResourcesRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CheckCustomizationResourcesRequestType from a JSON string
check_customization_resources_request_type_instance = CheckCustomizationResourcesRequestType.from_json(json)
# print the JSON string representation of the object
print CheckCustomizationResourcesRequestType.to_json()

# convert the object into a dict
check_customization_resources_request_type_dict = check_customization_resources_request_type_instance.to_dict()
# create an instance of CheckCustomizationResourcesRequestType from a dict
check_customization_resources_request_type_form_dict = check_customization_resources_request_type.from_dict(check_customization_resources_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


