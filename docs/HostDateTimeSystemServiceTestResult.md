# HostDateTimeSystemServiceTestResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**working_normally** | **bool** | Value is true if time services are presently working normally.  ***Since:*** vSphere API 7.0.3.0  | 
**report** | **List[str]** | Returns details of the checks done to verify time services are working.  ***Since:*** vSphere API 7.0.3.0  | [optional] 

## Example

```python
from vmware_vi.models.host_date_time_system_service_test_result import HostDateTimeSystemServiceTestResult

# TODO update the JSON string below
json = "{}"
# create an instance of HostDateTimeSystemServiceTestResult from a JSON string
host_date_time_system_service_test_result_instance = HostDateTimeSystemServiceTestResult.from_json(json)
# print the JSON string representation of the object
print HostDateTimeSystemServiceTestResult.to_json()

# convert the object into a dict
host_date_time_system_service_test_result_dict = host_date_time_system_service_test_result_instance.to_dict()
# create an instance of HostDateTimeSystemServiceTestResult from a dict
host_date_time_system_service_test_result_form_dict = host_date_time_system_service_test_result.from_dict(host_date_time_system_service_test_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


