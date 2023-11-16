# EstimateDatabaseSizeRequestType

The parameters of *ResourcePlanningManager.EstimateDatabaseSize*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**db_size_param** | [**DatabaseSizeParam**](DatabaseSizeParam.md) |  | 

## Example

```python
from vmware_vi.models.estimate_database_size_request_type import EstimateDatabaseSizeRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of EstimateDatabaseSizeRequestType from a JSON string
estimate_database_size_request_type_instance = EstimateDatabaseSizeRequestType.from_json(json)
# print the JSON string representation of the object
print EstimateDatabaseSizeRequestType.to_json()

# convert the object into a dict
estimate_database_size_request_type_dict = estimate_database_size_request_type_instance.to_dict()
# create an instance of EstimateDatabaseSizeRequestType from a dict
estimate_database_size_request_type_form_dict = estimate_database_size_request_type.from_dict(estimate_database_size_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


