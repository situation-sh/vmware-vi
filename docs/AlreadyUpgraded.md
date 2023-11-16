# AlreadyUpgraded

An AlreadyUpgraded fault is thrown when an attempt is made to upgrade the virtual hardware of a Virtual machine whose virtual hardware is already up-to-date. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.already_upgraded import AlreadyUpgraded

# TODO update the JSON string below
json = "{}"
# create an instance of AlreadyUpgraded from a JSON string
already_upgraded_instance = AlreadyUpgraded.from_json(json)
# print the JSON string representation of the object
print AlreadyUpgraded.to_json()

# convert the object into a dict
already_upgraded_dict = already_upgraded_instance.to_dict()
# create an instance of AlreadyUpgraded from a dict
already_upgraded_form_dict = already_upgraded.from_dict(already_upgraded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


