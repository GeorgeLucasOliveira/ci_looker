view: view_name {
  sql_table_name: schema.table ;;

   dimension: example {
    type: string
    description: "Dimension example"
    sql: ${TABLE}.column ;;
  }
}
