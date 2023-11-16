# InvalidBundle

An Invalid Bundle fault is thrown if an operation fails because of a problem with the supplied bundle.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.invalid_bundle import InvalidBundle

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidBundle from a JSON string
invalid_bundle_instance = InvalidBundle.from_json(json)
# print the JSON string representation of the object
print InvalidBundle.to_json()

# convert the object into a dict
invalid_bundle_dict = invalid_bundle_instance.to_dict()
# create an instance of InvalidBundle from a dict
invalid_bundle_form_dict = invalid_bundle.from_dict(invalid_bundle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


