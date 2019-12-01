# coding: utf-8


"""
Implement bulk insert and ON DUPLICATE KEY UPDATE statement
"""
class BulkQuery():


    def __init__(self, connection, table_name):

        self.__connection = connection
        self.__table_name = table_name
        self.__cursor = None
        self.__row_count = 0
        self.__column_names = []
        self.__values = []


    def add_record(self, record):
        """
        Add record: dict {column_name: value, column_name: value...}
        """
        if self.__row_count == 0:
            self.__column_names = record.keys()
        else:
            self.__column_name_check(record.keys())

        value_tuple = tuple(record.values())
        self.__values.append(value_tuple)
        self.__row_count += 1


    def insert_or_update(self):
        """
        Insert or update based on primary key or unique key
        """
        assigns = []
        for colmun_name in self.__column_names:
            assign = '`%s`=VALUES(`%s`)' % (colmun_name, colmun_name)
            assigns.append(assign)

        assigns_str = ','.join(assigns)
        ondpulicate_base = ' ON DUPLICATE KEY UPDATE %s' % assigns_str

        sql_base = ''.join([
            self.__insert_base_query(),
            ondpulicate_base
        ])

        self.get__cursor().executemany(sql_base, self.__values)
        return self


    def insert(self):
        """
        Bulk insert
        """
        sql_base = self.__insert_base_query()
        self.get__cursor().executemany(sql_base, self.__values)
        return self


    def __insert_base_query(self):

        column_size = len(self.__column_names)
        val_base = self.__comma_base(column_size, '%s')
        col_base = self.__comma_base(column_size, '`%s`')
        col_name_str = col_base % tuple(self.__column_names)

        query = 'INSERT INTO `%s`(%s)' % (self.__table_name ,col_name_str)
        query += ' VALUES(%s)' % (val_base)

        return query


    def save(self):
        """
        Query execution
        """
        self.__connection.commit()
        self.__cursor.close()

        try:
            self.__connection.commit()
        except Exception as e:
            self.__connection.rollback()
            raise e
        finally:
            self.__cursor.close()


    def get__cursor(self):

        if self.__cursor is None:
            self.__cursor = self.__connection.cursor()

        return self.__cursor


    def get__connection(self):

        return self.__connection


    def __comma_base(self, size, base):
        """
        return string %s,%s,...
        """
        return ','.join([base] * size)


    def __column_name_check(self, column_names):
        """
        params column_names: array
        """
        try:
            if self.__column_names != column_names:
                raise ValueError('Column name registered first is different from column name')
        except ValueError as e:
            print(e)

