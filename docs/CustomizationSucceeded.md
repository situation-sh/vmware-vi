# CustomizationSucceeded

The customization sequence completed successfully in the guest.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.customization_succeeded import CustomizationSucceeded

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizationSucceeded from a JSON string
customization_succeeded_instance = CustomizationSucceeded.from_json(json)
# print the JSON string representation of the object
print CustomizationSucceeded.to_json()

# convert the object into a dict
customization_succeeded_dict = customization_succeeded_instance.to_dict()
# create an instance of CustomizationSucceeded from a dict
customization_succeeded_form_dict = customization_succeeded.from_dict(customization_succeeded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


