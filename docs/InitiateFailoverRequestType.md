# InitiateFailoverRequestType

The parameters of *FailoverClusterManager.initiateFailover_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**planned** | **bool** | \\- if false, a failover is initiated immediate and may result in data loss. if true, a failover is initated after the Active node flushes its state to Passive and there is no data loss.  | 

## Example

```python
from vmware_vi.models.initiate_failover_request_type import InitiateFailoverRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of InitiateFailoverRequestType from a JSON string
initiate_failover_request_type_instance = InitiateFailoverRequestType.from_json(json)
# print the JSON string representation of the object
print InitiateFailoverRequestType.to_json()

# convert the object into a dict
initiate_failover_request_type_dict = initiate_failover_request_type_instance.to_dict()
# create an instance of InitiateFailoverRequestType from a dict
initiate_failover_request_type_form_dict = initiate_failover_request_type.from_dict(initiate_failover_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


