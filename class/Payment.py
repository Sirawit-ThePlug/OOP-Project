class Payment:
  def __init__ (self, amount, created_date_time, payment_options, transaction_id, payment_status ):
    self._amount = amount
    self._created_date_time = created_date_time
    self._payment_options = payment_options
    self._transaction_id = transaction_id
    self._payment_status = payment_status
