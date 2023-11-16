# LogBundlingFailed

A LogBundlingFailed exception is thrown when generation of a diagnostic data bundle fails. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.log_bundling_failed import LogBundlingFailed

# TODO update the JSON string below
json = "{}"
# create an instance of LogBundlingFailed from a JSON string
log_bundling_failed_instance = LogBundlingFailed.from_json(json)
# print the JSON string representation of the object
print LogBundlingFailed.to_json()

# convert the object into a dict
log_bundling_failed_dict = log_bundling_failed_instance.to_dict()
# create an instance of LogBundlingFailed from a dict
log_bundling_failed_form_dict = log_bundling_failed.from_dict(log_bundling_failed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


