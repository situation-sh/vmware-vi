# vmware_vi.LocalizationManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**localization_manager_get_catalog**](LocalizationManagerApi.md#localization_manager_get_catalog) | **GET** /LocalizationManager/{moId}/catalog | Fetches the descriptions of all the client-side localization message catalogs available for the current session locale. 


# **localization_manager_get_catalog**
> List[LocalizationManagerMessageCatalog] localization_manager_get_catalog(mo_id)

Fetches the descriptions of all the client-side localization message catalogs available for the current session locale. 

Fetches the descriptions of all the client-side localization message catalogs available for the current session locale.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.localization_manager_message_catalog import LocalizationManagerMessageCatalog
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.LocalizationManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Fetches the descriptions of all the client-side localization message catalogs available for the current session locale. 
        api_response = api_instance.localization_manager_get_catalog(mo_id)
        print("The response of LocalizationManagerApi->localization_manager_get_catalog:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocalizationManagerApi->localization_manager_get_catalog: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[LocalizationManagerMessageCatalog]**](LocalizationManagerMessageCatalog.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the message catalogs for the current locale  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

