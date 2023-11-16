# HttpFault

Generic base class for outbound HTTP communication errors.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **int** | HTTP status code received from external web-server.  ***Since:*** vSphere API 4.0  | 
**status_message** | **str** | HTTP status message received from external web-server.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.http_fault import HttpFault

# TODO update the JSON string below
json = "{}"
# create an instance of HttpFault from a JSON string
http_fault_instance = HttpFault.from_json(json)
# print the JSON string representation of the object
print HttpFault.to_json()

# convert the object into a dict
http_fault_dict = http_fault_instance.to_dict()
# create an instance of HttpFault from a dict
http_fault_form_dict = http_fault.from_dict(http_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


