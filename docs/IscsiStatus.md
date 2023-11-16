# IscsiStatus

The *IscsiStatus* data object describes the status of an operation.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | [**List[MethodFault]**](MethodFault.md) | List of failure reason and associated remedy.  An array of fault codes associated with the failure. The fault itself will provide an indication of the actual failure code and *MethodFault.faultMessage* will indicate the remedy that needs to be taken to correct the failure.  ***Since:*** vSphere API 5.0  | [optional] 

## Example

```python
from vmware_vi.models.iscsi_status import IscsiStatus

# TODO update the JSON string below
json = "{}"
# create an instance of IscsiStatus from a JSON string
iscsi_status_instance = IscsiStatus.from_json(json)
# print the JSON string representation of the object
print IscsiStatus.to_json()

# convert the object into a dict
iscsi_status_dict = iscsi_status_instance.to_dict()
# create an instance of IscsiStatus from a dict
iscsi_status_form_dict = iscsi_status.from_dict(iscsi_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


