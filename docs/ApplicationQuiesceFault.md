# ApplicationQuiesceFault

This fault is thrown when creating a quiesced snapshot failed because the (user-supplied) custom pre-freeze script in the virtual machine exited with a non-zero return code.  This indicates that the script failed to perform its quiescing task, which causes us to fail the quiesced snapshot operation. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.application_quiesce_fault import ApplicationQuiesceFault

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationQuiesceFault from a JSON string
application_quiesce_fault_instance = ApplicationQuiesceFault.from_json(json)
# print the JSON string representation of the object
print ApplicationQuiesceFault.to_json()

# convert the object into a dict
application_quiesce_fault_dict = application_quiesce_fault_instance.to_dict()
# create an instance of ApplicationQuiesceFault from a dict
application_quiesce_fault_form_dict = application_quiesce_fault.from_dict(application_quiesce_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


