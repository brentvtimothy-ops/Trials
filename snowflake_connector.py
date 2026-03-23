import snowflake.connector

# Function to establish a connection to Snowflake

def connect_to_snowflake(user, password, account):
    """Establishes a connection to Snowflake and returns the connection object."""
    conn = snowflake.connector.connect(
        user=user,
        password=password,
        account=account
    )
    return conn

# Function to execute a query and return the results

def execute_query(conn, query):
    """Executes a given SQL query and returns the results."""
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    finally:
        cursor.close()

# Function to close the connection

def close_connection(conn):
    """Closes the connection to Snowflake."""
    conn.close()

# Example usage:
if __name__ == '__main__':
    conn = connect_to_snowflake('YOUR_USER', 'YOUR_PASSWORD', 'YOUR_ACCOUNT')  # Replace with actual credentials
    try:
        results = execute_query(conn, 'SELECT CURRENT_VERSION()')
        print('Snowflake version:', results)
    finally:
        close_connection(conn)