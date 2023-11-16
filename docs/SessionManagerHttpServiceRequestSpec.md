# SessionManagerHttpServiceRequestSpec

This data object type describes a request to an HTTP or HTTPS service.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** | The HTTP method used for the request.  If null, then any method is assumed.  See also *SessionManagerHttpServiceRequestSpecMethod_enum*.  ***Since:*** vSphere API 5.0  | [optional] 
**url** | **str** | URL of the HTTP request.  E.g. &#39;https://127.0.0.1:8080/cgi-bin/vm-support.cgi?n&#x3D;val&#39;.  For ESXi CGI service requests: - only the path and query parts of the URL are used   (e.g. \&quot;/cgi-bin/vm-support.cgi?n&#x3D;val\&quot;).     This is so because the scheme is not known to the CGI service, and the port may not be the same if using a proxy.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.session_manager_http_service_request_spec import SessionManagerHttpServiceRequestSpec

# TODO update the JSON string below
json = "{}"
# create an instance of SessionManagerHttpServiceRequestSpec from a JSON string
session_manager_http_service_request_spec_instance = SessionManagerHttpServiceRequestSpec.from_json(json)
# print the JSON string representation of the object
print SessionManagerHttpServiceRequestSpec.to_json()

# convert the object into a dict
session_manager_http_service_request_spec_dict = session_manager_http_service_request_spec_instance.to_dict()
# create an instance of SessionManagerHttpServiceRequestSpec from a dict
session_manager_http_service_request_spec_form_dict = session_manager_http_service_request_spec.from_dict(session_manager_http_service_request_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


