# InvalidCollectorVersion

InvalidCollectorVersion is thrown when a collector version is out of date or invalid. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.invalid_collector_version import InvalidCollectorVersion

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidCollectorVersion from a JSON string
invalid_collector_version_instance = InvalidCollectorVersion.from_json(json)
# print the JSON string representation of the object
print InvalidCollectorVersion.to_json()

# convert the object into a dict
invalid_collector_version_dict = invalid_collector_version_instance.to_dict()
# create an instance of InvalidCollectorVersion from a dict
invalid_collector_version_form_dict = invalid_collector_version.from_dict(invalid_collector_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


