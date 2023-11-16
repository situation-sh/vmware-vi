# vmware_vi.SessionManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**session_manager_acquire_clone_ticket**](SessionManagerApi.md#session_manager_acquire_clone_ticket) | **POST** /SessionManager/{moId}/AcquireCloneTicket | Acquire a session-specific ticket string which can be used to clone the current session. 
[**session_manager_acquire_generic_service_ticket**](SessionManagerApi.md#session_manager_acquire_generic_service_ticket) | **POST** /SessionManager/{moId}/AcquireGenericServiceTicket | Creates and returns a one-time credential that may be used to make the specified request. 
[**session_manager_acquire_local_ticket**](SessionManagerApi.md#session_manager_acquire_local_ticket) | **POST** /SessionManager/{moId}/AcquireLocalTicket | Acquires a one-time ticket for mutual authentication between a server and client. 
[**session_manager_clone_session**](SessionManagerApi.md#session_manager_clone_session) | **POST** /SessionManager/{moId}/CloneSession | Clone the session specified by the clone ticket and associate it with the current connection. 
[**session_manager_get_current_session**](SessionManagerApi.md#session_manager_get_current_session) | **GET** /SessionManager/{moId}/currentSession | This property contains information about the client&#39;s current session. 
[**session_manager_get_default_locale**](SessionManagerApi.md#session_manager_get_default_locale) | **GET** /SessionManager/{moId}/defaultLocale | This is the default server locale. 
[**session_manager_get_message**](SessionManagerApi.md#session_manager_get_message) | **GET** /SessionManager/{moId}/message | The system global message from the server. 
[**session_manager_get_message_locale_list**](SessionManagerApi.md#session_manager_get_message_locale_list) | **GET** /SessionManager/{moId}/messageLocaleList | Provides the list of locales for which the server has localized messages. 
[**session_manager_get_session_list**](SessionManagerApi.md#session_manager_get_session_list) | **GET** /SessionManager/{moId}/sessionList | The list of currently active sessions. 
[**session_manager_get_supported_locale_list**](SessionManagerApi.md#session_manager_get_supported_locale_list) | **GET** /SessionManager/{moId}/supportedLocaleList | Provides the list of locales that the server supports. 
[**session_manager_impersonate_user**](SessionManagerApi.md#session_manager_impersonate_user) | **POST** /SessionManager/{moId}/ImpersonateUser | Converts current session to impersonate the specified user. 
[**session_manager_login**](SessionManagerApi.md#session_manager_login) | **POST** /SessionManager/{moId}/Login | Log on to the server. 
[**session_manager_login_by_sspi**](SessionManagerApi.md#session_manager_login_by_sspi) | **POST** /SessionManager/{moId}/LoginBySSPI | Log on to the server using SSPI pass-through authentication. 
[**session_manager_login_by_token**](SessionManagerApi.md#session_manager_login_by_token) | **POST** /SessionManager/{moId}/LoginByToken | Log on to the server through token representing principal identity. 
[**session_manager_login_extension**](SessionManagerApi.md#session_manager_login_extension) | **POST** /SessionManager/{moId}/LoginExtension | Creates a special privileged session that includes the Sessions.ImpersonateUser privilege. 
[**session_manager_login_extension_by_certificate**](SessionManagerApi.md#session_manager_login_extension_by_certificate) | **POST** /SessionManager/{moId}/LoginExtensionByCertificate | Creates a special privileged session that includes the Sessions.ImpersonateUser privilege. 
[**session_manager_login_extension_by_subject_name**](SessionManagerApi.md#session_manager_login_extension_by_subject_name) | **POST** /SessionManager/{moId}/LoginExtensionBySubjectName | Creates a special privileged session that includes the Sessions.ImpersonateUser privilege. 
[**session_manager_logout**](SessionManagerApi.md#session_manager_logout) | **POST** /SessionManager/{moId}/Logout | Log out and terminate the current session. 
[**session_manager_session_is_active**](SessionManagerApi.md#session_manager_session_is_active) | **POST** /SessionManager/{moId}/SessionIsActive | Validates that a currently-active session exists with the specified sessionID and userName associated with it. 
[**session_manager_set_locale**](SessionManagerApi.md#session_manager_set_locale) | **POST** /SessionManager/{moId}/SetLocale | Sets the session locale. 
[**session_manager_terminate_session**](SessionManagerApi.md#session_manager_terminate_session) | **POST** /SessionManager/{moId}/TerminateSession | Log off and terminate the provided list of sessions. 
[**session_manager_update_service_message**](SessionManagerApi.md#session_manager_update_service_message) | **POST** /SessionManager/{moId}/UpdateServiceMessage | Updates the system global message. 


# **session_manager_acquire_clone_ticket**
> str session_manager_acquire_clone_ticket(mo_id)

Acquire a session-specific ticket string which can be used to clone the current session. 

Acquire a session-specific ticket string which can be used to clone the current session.  The caller of this operation can pass the ticket value to another entity on the client. The recipient can then call *SessionManager.CloneSession* with the ticket string on an unauthenticated session and avoid having to re-enter credentials.  The ticket may only be used once and becomes invalid after use. The ticket is also invalidated when the corresponding session is closed or expires. The ticket is only valid on the server which issued it.  This sequence of operations is conceptually similar to the functionality provided by *SessionManager.AcquireLocalTicket*, however the methods can be used by remote clients and do not require a shared filesystem for transport.  See also *SessionManager.CloneSession*.  ***Since:*** VI API 2.5u2  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
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
    api_instance = vmware_vi.SessionManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Acquire a session-specific ticket string which can be used to clone the current session. 
        api_response = api_instance.session_manager_acquire_clone_ticket(mo_id)
        print("The response of SessionManagerApi->session_manager_acquire_clone_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionManagerApi->session_manager_acquire_clone_ticket: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

**str**

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | one-time secret ticket string.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **session_manager_acquire_generic_service_ticket**
> SessionManagerGenericServiceTicket session_manager_acquire_generic_service_ticket(mo_id, acquire_generic_service_ticket_request_type)

Creates and returns a one-time credential that may be used to make the specified request. 

Creates and returns a one-time credential that may be used to make the specified request.  ***Since:*** vSphere API 5.0  ***Required privileges:*** System.Anonymous 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.acquire_generic_service_ticket_request_type import AcquireGenericServiceTicketRequestType
from vmware_vi.models.session_manager_generic_service_ticket import SessionManagerGenericServiceTicket
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
    api_instance = vmware_vi.SessionManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    acquire_generic_service_ticket_request_type = vmware_vi.AcquireGenericServiceTicketRequestType() # AcquireGenericServiceTicketRequestType | 

    try:
        # Creates and returns a one-time credential that may be used to make the specified request. 
        api_response = api_instance.session_manager_acquire_generic_service_ticket(mo_id, acquire_generic_service_ticket_request_type)
        print("The response of SessionManagerApi->session_manager_acquire_generic_service_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionManagerApi->session_manager_acquire_generic_service_ticket: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **acquire_generic_service_ticket_request_type** | [**AcquireGenericServiceTicketRequestType**](AcquireGenericServiceTicketRequestType.md)|  | 

### Return type

[**SessionManagerGenericServiceTicket**](SessionManagerGenericServiceTicket.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | a ticket that may be used to invoke the specified request. The first choice for authenticating the host is *GenericServiceTicket#sslCertificate*. If *GenericServiceTicket#sslCertificate* is unset, the following logic is used to authenticate the host: 1\\. If the VC system supports the crypto hash algorithm of the *SessionManagerGenericServiceTicket.sslThumbprint* or *SessionManagerGenericServiceTicket.certThumbprintList* (if set), they will be verified against that of the server certificate. If they doesn&#39;t match, the CA certificates will be used to authenticate the host. 2\\. If the VC system does not support the crypto hash algorithm of *SessionManagerGenericServiceTicket.sslThumbprint* or *SessionManagerGenericServiceTicket.certThumbprintList*, only the CA certificates will be used to authenticate the host.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **session_manager_acquire_local_ticket**
> SessionManagerLocalTicket session_manager_acquire_local_ticket(mo_id, acquire_local_ticket_request_type)

Acquires a one-time ticket for mutual authentication between a server and client. 

Acquires a one-time ticket for mutual authentication between a server and client.  The caller of this operation can use the user name and file content of the returned object as the userName and password arguments for login operation. The local ticket that is returned becomes invalid either after it is used or after a server-determined ticket expiration time passes. This operation can be used by servers and clients to avoid re-entering user credentials after authentication by the operating system has already happened.  For example, service console utilities that connect to a host agent should not require users to re-enter their passwords every time the utilities run. Since the one-time password file is readable only by the given user, the identity of the one-time password user is protected by the operating system file permission.  Only local clients are allowed to call this operation. Remote clients receive an InvalidRequest fault upon calling this operation.  ***Required privileges:*** System.Anonymous 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.acquire_local_ticket_request_type import AcquireLocalTicketRequestType
from vmware_vi.models.session_manager_local_ticket import SessionManagerLocalTicket
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
    api_instance = vmware_vi.SessionManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    acquire_local_ticket_request_type = vmware_vi.AcquireLocalTicketRequestType() # AcquireLocalTicketRequestType | 

    try:
        # Acquires a one-time ticket for mutual authentication between a server and client. 
        api_response = api_instance.session_manager_acquire_local_ticket(mo_id, acquire_local_ticket_request_type)
        print("The response of SessionManagerApi->session_manager_acquire_local_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionManagerApi->session_manager_acquire_local_ticket: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **acquire_local_ticket_request_type** | [**AcquireLocalTicketRequestType**](AcquireLocalTicketRequestType.md)|  | 

### Return type

[**SessionManagerLocalTicket**](SessionManagerLocalTicket.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | LocalTicket object containing userName and path to file containing one-time password for use in login operation.  |  -  |
**500** | ***InvalidLogin***: if the userName is invalid.  ***NoPermission***: if the user and password are valid, but the user has no access granted.  ***NotSupported***: if the server does not support this operation.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **session_manager_clone_session**
> UserSession session_manager_clone_session(mo_id, clone_session_request_type)

Clone the session specified by the clone ticket and associate it with the current connection. 

Clone the session specified by the clone ticket and associate it with the current connection.  The current session will take on the identity and authorization level of the UserSession associated with the specified cloning ticket.  See also *SessionManager.AcquireCloneTicket*, *SessionManager.AcquireGenericServiceTicket*.  ***Since:*** VI API 2.5u2  ***Required privileges:*** System.Anonymous 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.clone_session_request_type import CloneSessionRequestType
from vmware_vi.models.user_session import UserSession
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
    api_instance = vmware_vi.SessionManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    clone_session_request_type = vmware_vi.CloneSessionRequestType() # CloneSessionRequestType | 

    try:
        # Clone the session specified by the clone ticket and associate it with the current connection. 
        api_response = api_instance.session_manager_clone_session(mo_id, clone_session_request_type)
        print("The response of SessionManagerApi->session_manager_clone_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionManagerApi->session_manager_clone_session: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **clone_session_request_type** | [**CloneSessionRequestType**](CloneSessionRequestType.md)|  | 

### Return type

[**UserSession**](UserSession.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The new/cloned UserSession object.  |  -  |
**500** | ***InvalidLogin***: if the specified ticket value is not valid.  ***NotSupported***: if the server does not support this operation.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **session_manager_get_current_session**
> UserSession session_manager_get_current_session(mo_id)

This property contains information about the client's current session. 

This property contains information about the client's current session.  If the client is not logged on, the value is null.  ***Required privileges:*** System.Anonymous 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.user_session import UserSession
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
    api_instance = vmware_vi.SessionManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # This property contains information about the client's current session. 
        api_response = api_instance.session_manager_get_current_session(mo_id)
        print("The response of SessionManagerApi->session_manager_get_current_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionManagerApi->session_manager_get_current_session: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**UserSession**](UserSession.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **session_manager_get_default_locale**
> str session_manager_get_default_locale(mo_id)

This is the default server locale. 

This is the default server locale.  ***Required privileges:*** System.Anonymous 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
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
    api_instance = vmware_vi.SessionManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # This is the default server locale. 
        api_response = api_instance.session_manager_get_default_locale(mo_id)
        print("The response of SessionManagerApi->session_manager_get_default_locale:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionManagerApi->session_manager_get_default_locale: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

**str**

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **session_manager_get_message**
> str session_manager_get_message(mo_id)

The system global message from the server. 

The system global message from the server.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
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
    api_instance = vmware_vi.SessionManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The system global message from the server. 
        api_response = api_instance.session_manager_get_message(mo_id)
        print("The response of SessionManagerApi->session_manager_get_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionManagerApi->session_manager_get_message: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

**str**

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **session_manager_get_message_locale_list**
> List[str] session_manager_get_message_locale_list(mo_id)

Provides the list of locales for which the server has localized messages. 

Provides the list of locales for which the server has localized messages.  ***Required privileges:*** System.Anonymous 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
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
    api_instance = vmware_vi.SessionManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Provides the list of locales for which the server has localized messages. 
        api_response = api_instance.session_manager_get_message_locale_list(mo_id)
        print("The response of SessionManagerApi->session_manager_get_message_locale_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionManagerApi->session_manager_get_message_locale_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

**List[str]**

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **session_manager_get_session_list**
> List[UserSession] session_manager_get_session_list(mo_id)

The list of currently active sessions. 

The list of currently active sessions.  ***Required privileges:*** Sessions.TerminateSession 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.user_session import UserSession
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
    api_instance = vmware_vi.SessionManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The list of currently active sessions. 
        api_response = api_instance.session_manager_get_session_list(mo_id)
        print("The response of SessionManagerApi->session_manager_get_session_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionManagerApi->session_manager_get_session_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[UserSession]**](UserSession.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **session_manager_get_supported_locale_list**
> List[str] session_manager_get_supported_locale_list(mo_id)

Provides the list of locales that the server supports. 

Provides the list of locales that the server supports.  Listing a locale ensures that some standardized information such as dates appear in the appropriate format. Other localized information, such as error messages, are displayed, if available. If localized information is not available, the message is returned using the system locale.  ***Required privileges:*** System.Anonymous 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
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
    api_instance = vmware_vi.SessionManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Provides the list of locales that the server supports. 
        api_response = api_instance.session_manager_get_supported_locale_list(mo_id)
        print("The response of SessionManagerApi->session_manager_get_supported_locale_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionManagerApi->session_manager_get_supported_locale_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

**List[str]**

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **session_manager_impersonate_user**
> UserSession session_manager_impersonate_user(mo_id, impersonate_user_request_type)

Converts current session to impersonate the specified user. 

Converts current session to impersonate the specified user.  The current session will take on the identity and authorization level of the user. That user must have a currently-active session. If the given userName is an extension key and this key does not overlap with a user name of any currently-active session, it will take on the identity and authorization level of that extension provided the current session has the same authorization level of that extension.  ***Since:*** VI API 2.5  ***Required privileges:*** Sessions.ImpersonateUser 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.impersonate_user_request_type import ImpersonateUserRequestType
from vmware_vi.models.user_session import UserSession
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
    api_instance = vmware_vi.SessionManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    impersonate_user_request_type = vmware_vi.ImpersonateUserRequestType() # ImpersonateUserRequestType | 

    try:
        # Converts current session to impersonate the specified user. 
        api_response = api_instance.session_manager_impersonate_user(mo_id, impersonate_user_request_type)
        print("The response of SessionManagerApi->session_manager_impersonate_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionManagerApi->session_manager_impersonate_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **impersonate_user_request_type** | [**ImpersonateUserRequestType**](ImpersonateUserRequestType.md)|  | 

### Return type

[**UserSession**](UserSession.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |
**500** | Failure  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **session_manager_login**
> UserSession session_manager_login(mo_id, login_request_type)

Log on to the server. 

Log on to the server.  This method fails if the user name and password are incorrect, or if the user is valid but has no permissions granted.  ***Required privileges:*** System.Anonymous 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.login_request_type import LoginRequestType
from vmware_vi.models.user_session import UserSession
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
    api_instance = vmware_vi.SessionManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    login_request_type = vmware_vi.LoginRequestType() # LoginRequestType | 

    try:
        # Log on to the server. 
        api_response = api_instance.session_manager_login(mo_id, login_request_type)
        print("The response of SessionManagerApi->session_manager_login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionManagerApi->session_manager_login: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **login_request_type** | [**LoginRequestType**](LoginRequestType.md)|  | 

### Return type

[**UserSession**](UserSession.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The UserSession object.  As of vSphere API 5.1 for VirtualCenter login use SSO style *SessionManager.LoginByToken*  |  -  |
**500** | ***InvalidLogin***: if the user and password combination is invalid.  ***NoPermission***: if the user is valid, but has no access granted.  ***InvalidLocale***: if the locale is invalid or unknown to the server.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **session_manager_login_by_sspi**
> UserSession session_manager_login_by_sspi(mo_id, login_by_sspi_request_type)

Log on to the server using SSPI pass-through authentication. 

Log on to the server using SSPI pass-through authentication.  This method provides support for passing credentials of the calling process to the server without using a password, by leveraging the Windows Security Support Provider Interface (SSPI) library.  If the function is not supported, this throws a NotSupported fault.  The client first calls AcquireCredentialsHandle(). If Kerberos is used, this should include the desired credential to pass. The client then calls InitializeSecurityContext(). The resulting partially-formed context is passed in Base-64 encoded form to this method.  If the context has been successfully formed, the server proceeds with login and behaves like *SessionManager.Login*. If further negotiation is needed, the server throws an SSPIChallenge fault with a challenge token, which the client should again pass to InitializeSecurityContext(), followed by calling this method again.  For more information, see the MSDN documentation on SSPI.  ***Since:*** VI API 2.5  ***Required privileges:*** System.Anonymous 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.login_by_sspi_request_type import LoginBySSPIRequestType
from vmware_vi.models.user_session import UserSession
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
    api_instance = vmware_vi.SessionManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    login_by_sspi_request_type = vmware_vi.LoginBySSPIRequestType() # LoginBySSPIRequestType | 

    try:
        # Log on to the server using SSPI pass-through authentication. 
        api_response = api_instance.session_manager_login_by_sspi(mo_id, login_by_sspi_request_type)
        print("The response of SessionManagerApi->session_manager_login_by_sspi:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionManagerApi->session_manager_login_by_sspi: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **login_by_sspi_request_type** | [**LoginBySSPIRequestType**](LoginBySSPIRequestType.md)|  | 

### Return type

[**UserSession**](UserSession.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The UserSession object.  As of vSphere API 5.1 for VirtualCenter login use SSO style *SessionManager.LoginByToken*  |  -  |
**500** | ***SSPIChallenge***: if further negotiation is required.  ***InvalidLogin***: if the user context could not be passed successfully, or the context is not valid on the server.  ***NoPermission***: if the user is valid, but has no access granted.  ***InvalidLocale***: if the locale is invalid or unknown to the server.  ***NotSupported***: if the service does not support SSPI authentication.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **session_manager_login_by_token**
> UserSession session_manager_login_by_token(mo_id, login_by_token_request_type)

Log on to the server through token representing principal identity. 

Log on to the server through token representing principal identity.  The token is obtained from SSO (single sign-on) service. This method fails if the token is not valid, or the principal has no permissions granted. Two type of sso tokens are supported by this method: Bearer and Holder-of-Key (HoK). If the token type obliges the method caller to prove his rights to present this token (HoK), then a signature is supplied as well. The token and the security signature if available are provided in a transport specific way.  If the communication with the VirtualCenter is SOAP based read the WS-Security specification (SAML Token profile) to understand how to transport the SSO token and signature.  Usual login scenario: 1. Acquire HoK token from the SSO service. Different authentication    mechanisms are available for acquiring token (user/password,    certificate, SSPI and so on). For more details consult the SSO    documentation. To find the location of your SSO service consult the    Virtual Infrastructure documentation. 2. Once SSO token is acquired successfully *SessionManager.LoginByToken* could be    invoked.     ***Since:*** vSphere API 5.1  ***Required privileges:*** System.Anonymous 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.login_by_token_request_type import LoginByTokenRequestType
from vmware_vi.models.user_session import UserSession
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
    api_instance = vmware_vi.SessionManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    login_by_token_request_type = vmware_vi.LoginByTokenRequestType() # LoginByTokenRequestType | 

    try:
        # Log on to the server through token representing principal identity. 
        api_response = api_instance.session_manager_login_by_token(mo_id, login_by_token_request_type)
        print("The response of SessionManagerApi->session_manager_login_by_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionManagerApi->session_manager_login_by_token: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **login_by_token_request_type** | [**LoginByTokenRequestType**](LoginByTokenRequestType.md)|  | 

### Return type

[**UserSession**](UserSession.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The UserSession object.  |  -  |
**500** | ***InvalidLogin***: if there is no token provided or the token could not be validated.  ***NoPermission***: if the principal is valid, but has no access granted.  ***InvalidLocale***: if the locale is invalid or unknown to the server.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **session_manager_login_extension**
> UserSession session_manager_login_extension(mo_id, login_extension_request_type)

Creates a special privileged session that includes the Sessions.ImpersonateUser privilege. 

Deprecated as of vSphere API 4.0, use SSO style of login instead *SessionManager.LoginByToken*.  Creates a special privileged session that includes the Sessions.ImpersonateUser privilege.  Requires exchange of a message signed with the extension's registered public key and base-64 encoded.  As of vSphere API 4.0, the NotFound fault is no longer thrown. Instead, InvalidLogin is thrown if the specified extension is not registered.  As of vSphere API 5.0, this method always throws a NotSupported exception.  ***Since:*** VI API 2.5  ***Required privileges:*** System.Anonymous 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.login_extension_request_type import LoginExtensionRequestType
from vmware_vi.models.user_session import UserSession
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
    api_instance = vmware_vi.SessionManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    login_extension_request_type = vmware_vi.LoginExtensionRequestType() # LoginExtensionRequestType | 

    try:
        # Creates a special privileged session that includes the Sessions.ImpersonateUser privilege. 
        api_response = api_instance.session_manager_login_extension(mo_id, login_extension_request_type)
        print("The response of SessionManagerApi->session_manager_login_extension:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionManagerApi->session_manager_login_extension: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **login_extension_request_type** | [**LoginExtensionRequestType**](LoginExtensionRequestType.md)|  | 

### Return type

[**UserSession**](UserSession.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |
**500** | Failure  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **session_manager_login_extension_by_certificate**
> UserSession session_manager_login_extension_by_certificate(mo_id, login_extension_by_certificate_request_type)

Creates a special privileged session that includes the Sessions.ImpersonateUser privilege. 

Deprecated as of vSphere API 6.0, use SSO style of login instead *SessionManager.LoginByToken*.  Creates a special privileged session that includes the Sessions.ImpersonateUser privilege.  Requires that the client connect over SSL and provide an X.509 certificate for which they hold the private key. The certificate must match the certificate used in an earlier call to *ExtensionManager.SetExtensionCertificate*.  NOTE: Verification of the received certificate (such as expiry, revocation, and trust chain) is not required for successful authentication using this method. If certificate verification is desired, use the *SessionManager.LoginExtensionBySubjectName* method instead.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.Anonymous 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.login_extension_by_certificate_request_type import LoginExtensionByCertificateRequestType
from vmware_vi.models.user_session import UserSession
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
    api_instance = vmware_vi.SessionManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    login_extension_by_certificate_request_type = vmware_vi.LoginExtensionByCertificateRequestType() # LoginExtensionByCertificateRequestType | 

    try:
        # Creates a special privileged session that includes the Sessions.ImpersonateUser privilege. 
        api_response = api_instance.session_manager_login_extension_by_certificate(mo_id, login_extension_by_certificate_request_type)
        print("The response of SessionManagerApi->session_manager_login_extension_by_certificate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionManagerApi->session_manager_login_extension_by_certificate: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **login_extension_by_certificate_request_type** | [**LoginExtensionByCertificateRequestType**](LoginExtensionByCertificateRequestType.md)|  | 

### Return type

[**UserSession**](UserSession.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |
**500** | ***InvalidLogin***: if the extension is not registered, or the certificate does not match the expected value.  ***InvalidLocale***: if the supplied locale is not valid  ***NoClientCertificate***: if no certificate was used by the client to connect  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **session_manager_login_extension_by_subject_name**
> UserSession session_manager_login_extension_by_subject_name(mo_id, login_extension_by_subject_name_request_type)

Creates a special privileged session that includes the Sessions.ImpersonateUser privilege. 

Deprecated as of vSphere API 6.0, use SSO style of login instead *SessionManager.LoginByToken*.  Creates a special privileged session that includes the Sessions.ImpersonateUser privilege.  Requires that the extension connected using SSL, with a certificate that has a subject name that matches the subject name registered for the extension.  As of vSphere API 4.0, the NotFound fault is no longer thrown. Instead, InvalidLogin is thrown if the specified extension is not registered.  ***Since:*** VI API 2.5  ***Required privileges:*** System.Anonymous 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.login_extension_by_subject_name_request_type import LoginExtensionBySubjectNameRequestType
from vmware_vi.models.user_session import UserSession
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
    api_instance = vmware_vi.SessionManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    login_extension_by_subject_name_request_type = vmware_vi.LoginExtensionBySubjectNameRequestType() # LoginExtensionBySubjectNameRequestType | 

    try:
        # Creates a special privileged session that includes the Sessions.ImpersonateUser privilege. 
        api_response = api_instance.session_manager_login_extension_by_subject_name(mo_id, login_extension_by_subject_name_request_type)
        print("The response of SessionManagerApi->session_manager_login_extension_by_subject_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionManagerApi->session_manager_login_extension_by_subject_name: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **login_extension_by_subject_name_request_type** | [**LoginExtensionBySubjectNameRequestType**](LoginExtensionBySubjectNameRequestType.md)|  | 

### Return type

[**UserSession**](UserSession.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |
**500** | ***InvalidLogin***: if the extension is not registered, or the subject name doesn&#39;t match the subject name of the extension.  ***InvalidLocale***: if the supplied locale is not valid  ***NotFound***: if no extension is associated with the given key  ***NoClientCertificate***: if no certificate was used by the client to connect  ***NoSubjectName***: if the extension was registered without a subject name  ***InvalidClientCertificate***: if the client cerificate fails the verification at the server  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **session_manager_logout**
> session_manager_logout(mo_id)

Log out and terminate the current session. 

Log out and terminate the current session.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
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
    api_instance = vmware_vi.SessionManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Log out and terminate the current session. 
        api_instance.session_manager_logout(mo_id)
    except Exception as e:
        print("Exception when calling SessionManagerApi->session_manager_logout: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **session_manager_session_is_active**
> bool session_manager_session_is_active(mo_id, session_is_active_request_type)

Validates that a currently-active session exists with the specified sessionID and userName associated with it. 

Validates that a currently-active session exists with the specified sessionID and userName associated with it.  Returns true if session exists.  ***Since:*** VI API 2.5  ***Required privileges:*** Sessions.ValidateSession 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.session_is_active_request_type import SessionIsActiveRequestType
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
    api_instance = vmware_vi.SessionManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    session_is_active_request_type = vmware_vi.SessionIsActiveRequestType() # SessionIsActiveRequestType | 

    try:
        # Validates that a currently-active session exists with the specified sessionID and userName associated with it. 
        api_response = api_instance.session_manager_session_is_active(mo_id, session_is_active_request_type)
        print("The response of SessionManagerApi->session_manager_session_is_active:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionManagerApi->session_manager_session_is_active: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **session_is_active_request_type** | [**SessionIsActiveRequestType**](SessionIsActiveRequestType.md)|  | 

### Return type

**bool**

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **session_manager_set_locale**
> session_manager_set_locale(mo_id, set_locale_request_type)

Sets the session locale. 

Sets the session locale.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.set_locale_request_type import SetLocaleRequestType
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
    api_instance = vmware_vi.SessionManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    set_locale_request_type = vmware_vi.SetLocaleRequestType() # SetLocaleRequestType | 

    try:
        # Sets the session locale. 
        api_instance.session_manager_set_locale(mo_id, set_locale_request_type)
    except Exception as e:
        print("Exception when calling SessionManagerApi->session_manager_set_locale: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **set_locale_request_type** | [**SetLocaleRequestType**](SetLocaleRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***InvalidLocale***: if the locale is invalid or unknown to the server.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **session_manager_terminate_session**
> session_manager_terminate_session(mo_id, terminate_session_request_type)

Log off and terminate the provided list of sessions. 

Log off and terminate the provided list of sessions.  This method is only transactional for each session ID. The set of sessions are terminated sequentially, as specified in the list. If a failure occurs, for example, because of an unknown sessionID, the method aborts with an exception. When the method aborts, any sessions that have not yet been terminated are left in their unterminated state.  ***Required privileges:*** Sessions.TerminateSession 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.terminate_session_request_type import TerminateSessionRequestType
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
    api_instance = vmware_vi.SessionManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    terminate_session_request_type = vmware_vi.TerminateSessionRequestType() # TerminateSessionRequestType | 

    try:
        # Log off and terminate the provided list of sessions. 
        api_instance.session_manager_terminate_session(mo_id, terminate_session_request_type)
    except Exception as e:
        print("Exception when calling SessionManagerApi->session_manager_terminate_session: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **terminate_session_request_type** | [**TerminateSessionRequestType**](TerminateSessionRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***NotFound***: if a sessionId could not be found as a valid logged-on session.  ***InvalidArgument***: if a sessionId matches the current session. Use the logout method to terminate the current session.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **session_manager_update_service_message**
> session_manager_update_service_message(mo_id, update_service_message_request_type)

Updates the system global message. 

Updates the system global message.  If not blank, the message is immediately displayed to currently logged-on users. When set, the message is shown by new clients upon logging in.  ***Required privileges:*** Sessions.GlobalMessage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_service_message_request_type import UpdateServiceMessageRequestType
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
    api_instance = vmware_vi.SessionManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_service_message_request_type = vmware_vi.UpdateServiceMessageRequestType() # UpdateServiceMessageRequestType | 

    try:
        # Updates the system global message. 
        api_instance.session_manager_update_service_message(mo_id, update_service_message_request_type)
    except Exception as e:
        print("Exception when calling SessionManagerApi->session_manager_update_service_message: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_service_message_request_type** | [**UpdateServiceMessageRequestType**](UpdateServiceMessageRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

